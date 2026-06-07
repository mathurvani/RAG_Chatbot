from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectordb = Chroma(
    persist_directory="vectordb",
    embedding_function=embedding_model
)

retriever = vectordb.as_retriever(
    search_kwargs={"k":3}
)