from typing import List, Tuple
import math

class VectorStoreItem:
    def __init__(self, embedding: List[float], document: str):
        self.embedding = embedding
        self.document = document


class VectorStore:
    def __init__(self):
        self.vector_store: List[VectorStoreItem] = []

    def add_embedding(self, embedding: List[float], document: str) -> None:
        self.vector_store.append(VectorStoreItem(embedding, document))

    def search(self, query_embedding: List[float], top_k: int = 3) -> List[str]:
        scored: List[Tuple[str, float]] = [
            (item.document, self.cosine_similarity(query_embedding, item.embedding))
            for item in self.vector_store
        ]
        # 按分数降序排列，取前 top_k
        top_k_documents = [doc for doc, _ in sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]]
        return top_k_documents

    @staticmethod
    def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        return dot_product / (norm_a * norm_b) if norm_a > 0 and norm_b > 0 else 0.0
