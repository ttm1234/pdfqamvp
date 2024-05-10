import json
import logging
import time
import functools

import flask


# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logdemo.log'),
        logging.StreamHandler(),
    ]
)


def unix_timestamp():
    return int(time.time() * 1000)


def result_handler(data, msg='not found', errcode=400):
    if data is None:
        r = {
            'code': errcode,
            'data': data,
            'msg': msg,
        }
    else:
        r = {
            'code': 200,
            'data': data,
            'msg': 'ok',
        }

    http_code = 200
    return flask.Response(response=json.dumps(r, indent=4, ensure_ascii=False), status=http_code,
                          mimetype='application/json')


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"[opt={func.__name__}, start_time={start_time}, execution_time={execution_time}]")
        return result

    return wrapper
