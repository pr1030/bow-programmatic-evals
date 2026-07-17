import psycopg2
from config.config import DB_CONFIG


class PostgresClient:
    def __init__(self):
        self.connection = None

    def connect(self):
        print("Connecting with:")
        print(DB_CONFIG)

        self.connection = psycopg2.connect(
            dbname=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def close(self):
        if self.connection:
            self.connection.close()