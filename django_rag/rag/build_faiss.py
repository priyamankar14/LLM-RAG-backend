

#New for ollama

import os
import pickle
import faiss
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from rag.models import Document
from rag.embeddings import embed

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
MAP_PATH = os.path.join(BASE_DIR, "id_map.pkl")

docs = list(Document.objects.all())

if not docs:
    raise ValueError("❌ No documents found. Run load_docs or load_wiki first.")

texts = [d.content for d in docs]
embeddings = embed(texts)

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(embeddings)

id_map = {i: docs[i].id for i in range(len(docs))}

faiss.write_index(index, INDEX_PATH)
with open(MAP_PATH, "wb") as f:
    pickle.dump(id_map, f)

print(f"✅ FAISS built with {len(docs)} documents")
