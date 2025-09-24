import os
import requests
from typing import List
from .vector_store import VectorStore
from sentence_transformers import SentenceTransformer



def log_title(title: str) -> None:
    print(f"\n===== {title} =====")


class EmbeddingRetriever:
    def __init__(self, embedding_model: str):
        self.embedding_model = embedding_model
        self.vector_store = VectorStore()
        self.model = SentenceTransformer(embedding_model)


    def embed_document(self, document: str) -> List[float]:
        log_title("EMBEDDING DOCUMENT")
        embedding = self._embed(document)
        self.vector_store.add_embedding(embedding, document)
        return embedding

    def embed_query(self, query: str) -> List[float]:
        log_title("EMBEDDING QUERY")
        return self._embed(query)

    def _embed(self, text: str) -> List[float]:
        embedding = self.model.encode(text).tolist()
        # print(embedding)
        return embedding


    def retrieve(self, query: str, top_k: int = 3) -> List[str]:
        query_embedding = self.embed_query(query)
        return self.vector_store.search(query_embedding, top_k)
