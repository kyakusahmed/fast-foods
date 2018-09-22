import requests, responses

import unittest
from app import Order

base_url = "http://127.0.0.1:5000/api/v1/orders"


class TestOrder(unittest.TestCase):
     

    def setUp(self):
        self.order = Order()

    def test_Order_class(self):
        self.assertIsInstance(self.order, Order)

    def test_get_orders(self):
        """Send GET request to the link."""
        response = requests.get(base_url)
        """If result is an instance of list (if it's a list), test should pass."""
        self.assertIsInstance(response.json().get('orders'), list)
        """If status code is 200, test passes."""
        self.assertEqual(response.status_code, 200)
       
    
    def test_get_order(self):
        response = requests.get(base_url + "/1")
        """Am expecting order key to be an instance of a list from the request response."""
        self.assertIsInstance(response.json().get('order'), list)
        self.assertEqual(response.status_code, 200)


    def test_add_order(self):
        data = {
            "date": "22/12/2010",
            "foodid": 34,
            "status": "pending",
            "userid": "ahmed"
        }
        response = requests.post(base_url, params=data)
        self.assertEqual(response.status_code, 201)

    def test_update_status(self):
        status = {
            
            "status": "pending"
        }
        response = requests.put(base_url +"/1", params = status)
        self.assertEqual(response.status_code, 200)
        

    def test_order_not_found(self):
      
        response = requests.get(base_url + "/45")
        self.assertEqual(response.json().get('message'), "order not found") 

    def test_update_order_not_found(self):
        response = requests.put(base_url + "/120")
        self.assertEqual(response.json().get('orders'), "Order not found")


        


   



   