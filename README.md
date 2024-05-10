
## 注意！！！！本项目使用的云api速度较慢，所以测试的时候需要等待较长时间

## 项目地址
https://github.com/ttm1234/pdfqamvp

## 配置文件
1.项目根目录手动创建 `config.txt.yaml`，内容参照 `_docs/config.txt.yaml.template` 的内容来更改  
2.项目根目录手动创建 `.env` ，内容参照 `_docs/.env.template` 的内容来更改  
> 注意：我用的是openai代理版本所以有 OPENAI_API_BASE

## 启动方式
1. 配置文件创建完成并保证无误后，本地测试直接启动 
```
python3 app.py
也可以使用 gunicorn 等启动
```
2.启动 celery worker，命令如下：
```
python3 -m celery worker -A celery_task -l INFO  --concurrency=20
```

之后访问 http://localhost:8000/pdfqamvp/ui/ 可以看到swagger-ui文档，

## 项目依赖
- SQLDB: 直接使用了sqlite，减少多余对外依赖。
- openai: 由于海内外上网环境的差异，我在配置文件中修改了 `OPENAI_API_KEY` 和 `OPENAI_API_BASE`。
- 阿里云大模型api，所以需要配置 `DASHSCOPE_API_KEY`
- langSmith，需要配置 `LANGCHAIN_API_KEY`
- sentry, 需要在 config.txt.yaml 配置 `sentry_dsn`
- celery, 需要在 config.txt.yaml 配置 `broker_url`
- redis, 需要在 config.txt.yaml 配置 redis 参数
- sqldb, 在 config.txt.yaml 中直接配置 `DB_CONFIG: 'sqlite:///sqlite.db'`
