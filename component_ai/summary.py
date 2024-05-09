from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from ._base import llm_tongyi, track_time, llm_openai


@track_time
def summarize_docs(docs):
    print('len(str(docs))', len(str(docs)))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100000, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)

    chain = load_summarize_chain(llm_openai, chain_type="map_reduce", verbose=True)
    r = chain.run(split_docs)

    print('summarize_pdf', type(r), str(r)[0: 1000])
    return r
