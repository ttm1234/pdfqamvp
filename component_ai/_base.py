from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms import Tongyi
from langchain_openai import OpenAI

import time
from functools import wraps
import dotenv
dotenv.load_dotenv()

llm_tongyi = Tongyi(model_name="qwen-plus")
llm_openai = OpenAI(temperature=0)

embeddings = DashScopeEmbeddings(
    model="text-embedding-v1",
)


def track_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"====Function '{func.__name__}' started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"====Function '{func.__name__}' ended at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"====Total time taken for '{func.__name__}': {end_time - start_time} seconds")
        return result
    return wrapper
