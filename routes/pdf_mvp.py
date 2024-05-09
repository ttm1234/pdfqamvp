from flask import request

from logics.pdf_mvp import get_file_detail, get_answer
from util import result_handler


def api_file_detail():
    user_pdf_id = request.args.to_dict()['user_pdf_id']

    r = get_file_detail(user_pdf_id)
    return result_handler(r)


def api_answer():
    args = request.args.to_dict()
    user_pdf_id = args['user_pdf_id']
    question = args['question']

    r = get_answer(user_pdf_id, question)
    return result_handler(r)
