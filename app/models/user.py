from app.models.connect import DatabaseConnection
from datetime import datetime


class User(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def register_user(self, first_name, last_name, email, password,role):
        try:
            command = """
            INSERT INTO USERS (first_name, last_name, email, password, role) VALUES('{}','{}','{}','{}','{}')
            """.format( first_name, last_name, email, password, role)
            self.cursor.execute(command)
            return "user registered successfully"
        except Exception as ex:
            return "failed {}".format(ex)

    def login_user(self, email, password):
        try:
            command = """
            SELECT * FROM users WHERE email= '{}' AND password = '{}'
            """.format(email, password)
            self.cursor.execute(command)
            user1 = self.cursor.fetchone()
            return user1
        except Exception as ex:
            return "failed {}".format(ex)    

    def view_user_history(self, user_id):
        command = """
        SELECT * from orders WHERE user_id = {}
        """.format(user_id)
        self.cursor.execute(command)
        order1 = self.cursor.fetchall()  
        return order1
    
    def delete_user(self, user_id):
        try:
            command = """
            DELETE from users WHERE user_id = {}
            """.format(user_id)
            self.cursor.execute(command)
            return  "data deleted"
        except Exception as ex:
            return "failed {}".format(ex)

    def place_order(self, user_id, quantity, location, status, created_at):
            command = """
            INSERT INTO orders (user_id, quantity, location, status, created_at)  VALUES('{}', '{}', '{}', '{}','{}')
            """.format(user_id, quantity, location, status, str(datetime.now()))
            self.cursor.execute(command)
            return "order is placed"

    def find_user(self, user_id):
        command = """
        SELECT * from users WHERE user_id ={}
        """.format(user_id)
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

    def find_user_by_email(self, email):
        command = """
        SELECT * from users WHERE email ={}
        """.format(email)
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        return data

   
        
    
    
