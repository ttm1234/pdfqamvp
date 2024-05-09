import time

from models import UserPdf
import component_ai


def get_file_detail(_id):
    user_pdf: UserPdf = UserPdf.get_one(_id)

    return user_pdf.to_dict()


def process_pdf(_id):
    user_pdf: UserPdf = UserPdf.get_one(_id)
    if user_pdf.processed:
        return True

    # ----------------------------
    docs = component_ai.docs_from_pdf(user_pdf.full_filename)
    # component_ai.generate_vectorstore(user_pdf.id, docs)
    summary = component_ai.summarize_docs(docs)
    user_pdf.update_status(summary)
    # for i in range(20):
    #     print('sleep', i)
    #     time.sleep(60)
    return True


def get_answer(_id, question):
    user_pdf: UserPdf = UserPdf.get_one(_id)
    assert user_pdf is not None

    vectorstore = component_ai.load_vectorstore(user_pdf.id)

    answer = component_ai.get_rag_answer(vectorstore, question)

    r = {
        'user_pdf_id': _id,
        'question': question,
        'answer': answer,
    }
    return r

