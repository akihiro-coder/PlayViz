"""テスト環境用の設定"""
from .default import DefaultConfig


class TestingConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
