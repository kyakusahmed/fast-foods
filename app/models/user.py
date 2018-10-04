from app.models.connect import DatabaseConnection
from datetime import datetime
from flask import jsonify

class Admin(DatabaseConnection):

    def __init__(self):
        super().__init__()

    def get_all_orders(self):
        command = """
        select row_to_json(row) from (SELECT * FROM orders) row 
        """
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def get_one_order(self, orders_id):
        command = """
        SELECT * FROM ORDERS WHERE orders_id = {}
        """.format(orders_id)  
        self.cursor.execute(command)
        return self.cursor.fetchone() 



    def update_order_status(self, orders_id, status):
        command = "UPDATE orders SET status = '%s' WHERE orders_id = '%s'" % (status, orders_id)
        self.cursor.execute(command)
        return "status updated"
        


    def add_meal(self, food_title, description, price, status):
        try:
            command = """
            INSERT INTO MENU (food_title, description, price, status) VALUES('{}', '{}', '{}', '{}')
            """.format(food_title, description, price, status)
            self.cursor.execute(command)
            return "Data Inserted Successfully"
        except Exception as ex:
            return "failed {}".format(ex)

    def get_menu(self):
        try:
            command= "SELECT * FROM MENU"
            self.cursor.execute(command)
            menu = self.cursor.fetchall()
            return menu
        except Exception as ex:
            return "failed {}".format(ex)



