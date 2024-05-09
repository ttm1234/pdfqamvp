from flask import request

from logics.upload import receive_file
from util import result_handler


def api_upload():
    file = request.files['file']

    # print('file', type(file))

    r = receive_file(file)
    return result_handler(r)
