from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

db = Chroma(
    persist_directory="vectordb",
    embedding_function=embedding
)


def search_vector(query):

    docs = db.similarity_search(query, k=3)

    print("\n===== RETRIEVED DOCUMENTS FROM CHROMA =====\n")

    context = "\n".join([doc.page_content for doc in docs])

    return context