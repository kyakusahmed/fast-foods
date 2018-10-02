from datetime import datetime

class Order():
    
    def __init__(self, orders=[]):
        self.orders = orders

    def add_order(self, food_name, userid, status):
        order1 = {
            "id" : len(self.orders) + 1,
            "food_name" : food_name,
            "userid" : userid,
            "date" : str(datetime.now()),
            "status" : status
        }
        self.orders.append(order1)
        return order1

    def get_order(self, id):
        return self.search_order(id)

    def remove_order(self, id):
        for order in self.orders:
            if order['id'] == id:
                return self.orders.remove(order)
            return {'message':'list empty'}
         
    def return_all_orders(self):
        return self.orders
        
    def search_order(self, id):
        order = [order for order in self.orders if order['id'] == id]
        if order:
            return order
        return None

    def update_status(self, id, status):
        """Search for order."""
        order = self.search_order(id)
        """If exists, update status to new status."""
        if order:
            order[0].update({"status": status})
            return order
        return "Order not found"        

        