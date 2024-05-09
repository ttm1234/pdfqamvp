from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from ._base import llm_tongyi, track_time, llm_openai


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


@track_time
def get_rag_answer(vectorstore, question):
    retriever = vectorstore.as_retriever()
    prompt = hub.pull("rlm/rag-prompt")

    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm_openai
            | StrOutputParser()
    )
    r = rag_chain.invoke(question)
    print('get_rag_answer==', question, str(r)[0: 1000])
    return r
