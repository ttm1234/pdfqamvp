from langchain_community.document_loaders import PyMuPDFLoader

from ._base import track_time, log_execution_time


@track_time
@log_execution_time
def docs_from_pdf(full_filename):
    loader = PyMuPDFLoader(file_path=full_filename)
    docs = loader.load()
    print('docs_from_pdf', str(docs)[0: 100])
    return docs

