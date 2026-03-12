# from langchain.vectorstores import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings

# embedding_model = HuggingFaceEmbeddings(
#     model_name="BAAI/bge-small-en-v1.5"
# )

# db = Chroma(
#     persist_directory="vectordb",
#     embedding_function=embedding_model
# )

# def search_vector(query):
#     docs = db.similarity_search(query, k=3)
#     return "\n".join([d.page_content for d in docs])

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

db = Chroma(
    persist_directory="vectordb",
    embedding_function=embedding_model
)

def search_vector(query):

    docs = db.similarity_search(query, k=3)

    print("\nTop Retrieved Chunks:\n")

    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}:\n")
        print(doc.page_content[:500])

    return "\n".join([d.page_content for d in docs])