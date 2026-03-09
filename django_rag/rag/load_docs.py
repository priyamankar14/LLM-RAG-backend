from rag.models import Document

docs = [
    ("ML", "Machine learning is a field of artificial intelligence that learns from data."),
    ("DL", "Deep learning is a subset of machine learning using neural networks."),
    ("RAG", "RAG stands for Retrieval Augmented Generation."),
    ("FAISS", "FAISS is a library for fast vector similarity search.")
]

for title, content in docs:
    Document.objects.create(title=title, content=content)

print("Documents inserted successfully")
