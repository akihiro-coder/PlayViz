"""環境ごとの設定を切り替えるロジック"""

import os


def load_config():
    env = os.getenv('FLASK_DEBUG', 'default')  # 環境変数から取得（デフォルトは "default"）
    if env == 1:
        from .development import DevelopmentConfig
        return DevelopmentConfig
    elif env == 0:
        from .production import ProductionConfig
        return ProductionConfig
    else:
        from .testing import TestingConfig
        return TestingConfig
    # else:
    #     from .default import DefaultConfig
    #     return DefaultConfig