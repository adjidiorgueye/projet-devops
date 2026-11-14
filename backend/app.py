import os
import psycopg
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello depuis mon backend DevOps !"


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/db-health")
def db_health():
    try:
        conn = psycopg.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            user=os.getenv("DB_USER", "devops"),
            password=os.getenv("DB_PASSWORD", "devops123"),
            dbname=os.getenv("DB_NAME", "projet")
        )

        conn.close()

        return {"database": "ok"}

    except Exception as e:
        return {"database": "error", "message": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
