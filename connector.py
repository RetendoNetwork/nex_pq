import psycopg2
from psycopg2 import OperationalError

class PostgresConnector:
    def __init__(self, dbname, user, password, host, port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to Postgres Database !")
        except OperationalError as e:
            print(f"Error connecting to database : {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Disconnected to Postgres Database !")