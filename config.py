import yaml
import prerun_hooks


prerun_hooks.load_and_patch_all()


path = 'config.txt.yaml'
with open(path, encoding='utf-8') as f:
    yaml_conf = yaml.safe_load(f)
    # print(type(yaml_conf), yaml_conf)


class Config(object):
    upload_folder = 'file_upload'

    def __init__(self):
        self.dev = yaml_conf['dev']

        self.flask_secret_key = yaml_conf['flask_secret_key']
        self.jwt_secret = yaml_conf['jwt_secret']
        self.broker_url = yaml_conf['broker_url']
        self.DB_CONFIG = yaml_conf['DB_CONFIG']

        self.redis_host = yaml_conf['redis_host']
        self.redis_port = yaml_conf['redis_port']
        self.redis_db = yaml_conf['redis_db']
        self.redis_password = yaml_conf['redis_password']

        self.sentry_dsn = yaml_conf['sentry_dsn']


config = Config()
