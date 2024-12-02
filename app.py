from dotenv import load_dotenv
from baseball_app import create_app, db


# .envを読み込む
load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run()
