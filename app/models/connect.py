import psycopg2



class DatabaseConnection:
 
    def __init__(self):
        try:
            # self.conn = psycopg2.connect(
            # database="d4mdo559tepgh4", user="", password="a70ece5c8d7911994e3027aa8fef4d57a1fa07dcbc4c3208b19e165701a572e3", port="5432", host="ec2-54-243-147-162.compute-1.amazonaws.com"
            # )
            # self.conn.autocommit = True
            # self.cursor = self.conn.cursor()
            # print("connected")

            self.conn = psycopg2.connect(
            database="ahmad", user="postgres", password="1988", port="5432", host="127.0.0.1"
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("connected")
        except Exception as ex:
            print("connection failed {}".format(ex))



