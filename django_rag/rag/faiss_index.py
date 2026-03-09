# import faiss
# import numpy as np
# import pickle
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
# MAP_PATH = os.path.join(BASE_DIR, "id_map.pkl")

# def load_faiss():
#     if not os.path.exists(INDEX_PATH) or not os.path.exists(MAP_PATH):
#         dim = 384
#         index = faiss.IndexFlatL2(dim)
#         return index, {}

#     index = faiss.read_index(INDEX_PATH)
#     with open(MAP_PATH, "rb") as f:
#         id_map = pickle.load(f)

#     return index, id_map


# def search_embedding(query_embedding, k=3):
#     index, id_map = load_faiss()

#     if index.ntotal == 0:
#         return []

#     D, I = index.search(query_embedding, min(k, index.ntotal))

#     if len(I) == 0 or len(I[0]) == 0:
#         return []

#     return [id_map[i] for i in I[0]]


