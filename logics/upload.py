import hashlib
import os
from werkzeug.datastructures.file_storage import FileStorage

from config import config
from models import UserPdf


def md5_from_file(file: FileStorage):
    md5_hash = hashlib.md5()

    # 使用循环逐块更新哈希对象
    while chunk := file.read(4096):
        md5_hash.update(chunk)

    file_hash = md5_hash.hexdigest()
    file.seek(0)
    # print('file_hash', type(file_hash), file_hash)
    return file_hash


def receive_file(file: FileStorage):
    filename = file.filename

    if filename == '':
        return "No selected file", 400

    file_md5 = md5_from_file(file)
    file.seek(0)

    user_pdf: UserPdf = UserPdf.one_from_md5(file_md5)
    if user_pdf is None:
        # 保存文件
        full_filename = os.path.join(config.upload_folder, file_md5 + filename)
        file.save(full_filename)

        user_pdf = UserPdf.create(filename, file_md5, full_filename)

        import celery_task
        r = celery_task.celery_process_pdf1.delay(user_pdf.id)
        print('celery_task.celery_process_pdf.delay', r)

    else:
        pass

    return user_pdf.to_dict()
