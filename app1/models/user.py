from app1.models.connect import DatabaseConnection
import datetime

class User(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def register_user(self, first_name, last_name, email, password,role):
        command = """
        INSERT INTO USERS (first_name, last_name, email, password, role) VALUES('{}','{}','{}','{}','{}')
        """.format( first_name, last_name, email, password, role)
        self.cursor.execute(command)
        return "user registered successfully"

    def login_user(self, email, password):
        command = """
        SELECT * FROM users WHERE email= '{}' AND password= '{}'
        """.format(email, password)
        self.cursor.execute(command)
        user = self.cursor.fetchone()
        return user

    def view_user_history(self, user_id):
        command = """
        SELECT * from orders WHERE user_id = {}
        """.format(user_id)
        self.cursor.execute(command)
        data = self.cursor.fetchall()  
        return data      

    def delete_user(self, userd_id):
        try:
            command = """
            DELETE from users WHERE user_id = {}
            """.format(userd_id)
            self.cursor.execute(command)
            return  "data deleted"
        except Exception as ex:
            return "failed {}".format(ex)

    def place_order(self, user_id, quantity, location, status, created_at):
            command = """
            INSERT INTO orders (user_id, quantity, location, status, created_at)  VALUES('{}', '{}', '{}', '{}','{}')
            """.format(user_id, quantity, location, status, created_at)
            self.cursor.execute(command)
            return "order is placed"

    def find_user(self, user_id):
        command = """
        SELECT * from users WHERE user_id ={}
        """.format(user_id)
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    
