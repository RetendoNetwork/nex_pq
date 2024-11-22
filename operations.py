from psycopg2 import sql
from .connector.py import PostgresConnector
from .errors import CreateDatabaseError, CreateTableError, InsertDataError

class PostgresOperations(PostgresConnector):
    def create_database(self, new_dbname):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname)))
                self.conn.commit()
                print(f"Database '{new_dbname}' created successfully !")
        except Exception as e:
            raise CreateDatabaseError(f"Error creating database : {e}")

    def create_table(self, table_name, columns):
        try:
            with self.conn.cursor() as cursor:
                columns_with_types = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
                cursor.execute(sql.SQL("CREATE TABLE {} ({})").format(
                    sql.Identifier(table_name),
                    sql.SQL(columns_with_types)
                ))
                self.conn.commit()
                print(f"Table '{table_name}' created successfully !")
        except Exception as e:
            raise CreateTableError(f"Error creating table : {e}")

    def insert_data(self, table_name, data):
        try:
            with self.conn.cursor() as cursor:
                columns = data.keys()
                values = [data[col] for col in columns]
                insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
                    sql.Identifier(table_name),
                    sql.SQL(', ').join(map(sql.Identifier, columns)),
                    sql.SQL(', ').join(sql.Placeholder() * len(values))
                )
                cursor.execute(insert_query, values)
                self.conn.commit()
                print(f"Data inserted into table '{table_name}' v")
        except Exception as e:
            raise InsertDataError(f"Error inserting data : {e}")