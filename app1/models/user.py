from app.models.connect import DatabaseConnection

class User(DatabaseConnection):

    def __init__(self):
        super().__init__()


    def register_user(self, first_name, last_name, email, password):
        command = """
        INSERT INTO USERS (first_name, last_name, email, password, role) VALUES('{}','{}','{}','{}','{}')
        """.format( first_name, last_name, email, password, "0")
        self.cursor.execute(command)
        return "user registered successfully"

    def login_user(self, email, password):
        command = """
        SELECT * FROM users WHERE email= '{}' AND password= '{}'
        """.format(email, password)
        self.cursor.execute(command)
        user = self.cursor.fetchone()
        return user
