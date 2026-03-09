from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    embeddings = model.encode(texts, convert_to_numpy=True)
    faiss.normalize_L2(embeddings)
    return embeddings
