"""テスト環境用の設定"""
from .default import DefaultConfig


class TestingConfig(DefaultConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
