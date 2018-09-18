


     
class Order( ):
    def __init__(self, orders = []):
        self.orders = orders
       
        
        
        
    def add_order(self, id, foodid, userid, date, status):

        order = {
            "id" : id,
            "foodid" : foodid,
            "userid" : userid,
            "date" : date,
            "status" : status
        }
        self.orders.append(order)
        return self.orders
     
        
    def get_order(self, id):
        for order in self.orders:
            if order['id'] == id:
                return order
            else:
                return None
        
        
    def remove_order(self, id):
        for order in self.orders:
            if order['id'] == id:
                return self.orders.remove(order)
            return ({'message':'list empty'})
         
        
    def return_all_orders(self):
        return self.orders
         
    
    
    def search_order(self, id):
        order = [order for order in self.orders if order['id'] == id]
        if order:
            return order
        return None