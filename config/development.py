"""開発環境用の設定"""
from .default import DefaultConfig


class DevelopmentConfig(DefaultConfig):
    FLASK_DEBUG = 1
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'