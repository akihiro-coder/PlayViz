# APP_NAME = 'PlayViz'
# LOG_FILE = 'appserver.log'
# SECRET_KEY = '1111'
# PORT = 5000


"""デフォルトの設定値"""
class DefaultConfig:
    SECRET_KEY = '1111'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///default.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False