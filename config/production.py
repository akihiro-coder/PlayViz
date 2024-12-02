"""本番環境用の設定"""
from .default import DefaultConfig


class ProductionConfig(DefaultConfig):
    FLASK_DEBUG = 0
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/prod_db'
