from argoagent.rag.embedding_retriever import EmbeddingRetriever

def main():
    # 初始化检索器（传入模型名字）
    retriever = EmbeddingRetriever(embedding_model="all-MiniLM-L6-v2")


    # 添加一些文档到向量库
    docs = [
        "Python is widely used for web development, data analysis, and AI research.",
        "Machine learning allows systems to improve performance over time by learning patterns from historical data.",
        "Paris, located on the River Seine, is the largest city and cultural hub of France.",
        "Modern AI agents leverage Large Language Models to understand natural language and assist in decision making.",
    ]

    # 将文档嵌入
    for doc in docs:
        retriever.embed_document(doc)

    # 查询示例（更难，需要推理）
    query = "Which city, known for its art and the Eiffel Tower, serves as the capital of France?"

    results = retriever.retrieve(query, top_k=2)

    print("\n--- Query ---")
    print(query)
    print("\n--- Retrieved Documents ---")
    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc}")


if __name__ == "__main__":
    main()
