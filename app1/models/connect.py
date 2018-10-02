import psycopg2

class DatabaseConnection:
 
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
            database="ahmad", user="ahmed", password="1988", port="5432", host="localhost"
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("connected")
        except Exception as ex:
            print("connection failed {}".format(ex))