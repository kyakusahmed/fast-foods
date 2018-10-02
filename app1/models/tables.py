from app.models.connect import DatabaseConnection

class Migration(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def create_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = (
        """ CREATE TABLE USERS (
            USER_ID SERIAL PRIMARY KEY,
            FIRST_NAME VARCHAR(50) NOT NULL,
            LAST_NAME VARCHAR(50) NOT NULL,
            EMAIL VARCHAR(50),
            PASSWORD VARCHAR(50),
            ROLE VARCHAR(50),
            CREATED_AT DATE
            )
        """,
        """ CREATE TABLE MENU (
                MENU_ID INTEGER PRIMARY KEY,
                FOOD_TITLE VARCHAR(50),
                DESCRIPTION VARCHAR(500) NOT NULL,
                PRICE VARCHAR(50) NOT NULL,
                STATUS VARCHAR(50) ,
                USER_ID INTEGER REFERENCES USERS(USER_ID)
        )
        """,
        """ CREATE TABLE ORDERS (
                ORDERS_ID INTEGER NOT NULL,
                USER_ID INTEGER REFERENCES USERS(USER_ID),
                QUANTITY VARCHAR(50),
                LOCATION VARCHAR(50),
                STATUS VARCHAR(50),
                CREATED_AT DATE
        )
        """)

        for command in commands:
            self.cursor.execute(command)
