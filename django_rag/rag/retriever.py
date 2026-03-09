

#new for ollama


import os, pickle, faiss
from rag.embeddings import embed
from rag.models import Document

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
MAP_PATH = os.path.join(BASE_DIR, "id_map.pkl")

def retrieve(query, top_k=3, threshold=0.25):
    if not os.path.exists(INDEX_PATH):
        return []

    index = faiss.read_index(INDEX_PATH)
    with open(MAP_PATH, "rb") as f:
        id_map = pickle.load(f)

    query_embedding = embed([query])
    scores, indices = index.search(query_embedding, top_k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if score < threshold:
            continue

        doc_id = id_map[idx]
        doc = Document.objects.get(id=doc_id)

        results.append({
            "content": doc.content,
            "score": float(score)
        })

    return results
