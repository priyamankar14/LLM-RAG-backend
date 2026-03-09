from django.core.management.base import BaseCommand
from pathlib import Path
from rag.models import Document

CHUNK_SIZE = 400  # words


def chunk_text(text, chunk_size=400):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])


class Command(BaseCommand):
    help = "Load Simple Wikipedia dataset into Document table"

    def handle(self, *args, **kwargs):
        base_dir = Path.cwd().parent   # LLM/
        wiki_dir = base_dir / "archive"

        if not wiki_dir.exists():
            self.stderr.write(f"❌ Folder not found: {wiki_dir}")
            return

        self.stdout.write(f"📂 Reading data from: {wiki_dir}")

        total_chunks = 0

        for file in wiki_dir.rglob("*.txt"):
            self.stdout.write(f"✔ Processing: {file.name}")

            try:
                text = file.read_text(encoding="utf-8", errors="ignore")
            except Exception as e:
                self.stderr.write(f"⚠ Failed to read {file.name}: {e}")
                continue

            for chunk in chunk_text(text, CHUNK_SIZE):
                if len(chunk.strip()) < 50:
                    continue

                Document.objects.create(
                    title=file.name,
                    content=chunk
                )
                total_chunks += 1

        self.stdout.write(f"\n✅ Total chunks inserted: {total_chunks}")
