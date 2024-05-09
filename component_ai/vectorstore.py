from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from ._base import embeddings, track_time


def _get_vectorstore_filename(_id):
    return f"./file_vectorstore/vectorstore_{_id}"


@track_time
def generate_vectorstore(_id, docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=_get_vectorstore_filename(_id),
    )

    print('generate_vectorstore', type(vectorstore))

    return vectorstore


@track_time
def load_vectorstore(_id):
    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory=_get_vectorstore_filename(_id),
    )
    print('load_vectorstore', type(vectorstore))
    return vectorstore
