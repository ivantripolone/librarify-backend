# wsgi.py
from app import create_app

app = create_app('config.development.DevelopmentConfig')

if __name__ == "__main__":
    app.run()
