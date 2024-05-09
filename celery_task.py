from extensions.celery_conn import celery_app
from logics.pdf_mvp import process_pdf


@celery_app.task()
def celery_hello(*args, **kwargs):
    print('celery hello world', args, kwargs)


@celery_app.task(
    autoretry_for=(Exception,),
    max_retries=1,
    retry_backoff=5,
    retry_backoff_max=60 * 10,
    retry_jitter=False,
)
def celery_process_pdf1(user_pdf_id: int):
    print('celery_process_pdf start', user_pdf_id)
    return process_pdf(user_pdf_id)


'''
python3 -m celery worker -A celery_task -l INFO --pool=gevent --concurrency=10
python3 -m celery worker -A celery_task -l INFO  --concurrency=10
'''