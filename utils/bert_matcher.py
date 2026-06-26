
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_semantic_score(resume,jd):
    r = model.encode([resume])
    j = model.encode([jd])
    return cosine_similarity(r,j)[0][0]*100
