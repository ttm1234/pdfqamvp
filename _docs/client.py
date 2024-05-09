import json

import requests

base_url = 'http://localhost:8000/pdfqamvp'


def response_log(r: requests.Response):
    try:
        print(json.dumps(r.json(), indent=4, ensure_ascii=False))
    except Exception as e:
        print(r.status_code, r.content)


headers = {
}


def upload_file():
    url = base_url + '/upload'

    filename = 'pdf-large.pdf'
    with open(filename, 'rb') as file:
        files = {'file': file}
        r = requests.post(url, files=files)
        response_log(r)


def get_detail():
    url = base_url + '/detail'
    data = {
        'user_pdf_id': 2,
    }
    r = requests.get(url, params=data, headers=headers)
    response_log(r)


def get_answer():
    url = base_url + '/answer'

    # msg = 'Give me a summary of chapter 7.'
    # msg = 'Give me a summary of chapter 7: Designing the Document'
    # msg = 'How many kinds of typefaces are mentioned in this document'
    msg = 'How many kinds of typefaces are mentioned in chapter 7 Designing the Document'

    data = {
        'user_pdf_id': 1,
        'question': msg,
    }
    r = requests.get(url, params=data, headers=headers)
    response_log(r)


if __name__ == '__main__':
    upload_file()
    # get_detail()
    # get_answer()

