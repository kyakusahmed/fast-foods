import unittest
import requests

"""import base_url"""
base_url = "https://ahmad-fast-food-fast.herokuapp.com/api/v1/orders"

"""testing Order class"""
class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = [
            {
                "id": 1,
                "foodid": 24,
                "userid": 6,
                "date": "12/02/2018",
                "status": "pending"
            }
        ]

    def test_get_orders(self):
        """Send GET request to the link."""
        response = requests.get(base_url)
        self.assertIsInstance(response.json().get('orders'), list)
        self.assertEqual(response.status_code, 200)
      
    def test_get_order(self):
        response = requests.get(base_url + "/1")
        """Am expecting order key to be an instance of a list from the request response."""
        self.assertIsInstance(response.json().get('order'), list)
        self.assertEqual(response.status_code, 200)
        """post the specific data to the orders list"""
    def test_add_order(self):
        data = {
            "foodid": 34,
            "status": "pending",
            "userid": "ahmed"
        }
        response = requests.post(base_url, params=data)
        self.assertEqual(response.json().get('orders')['userid'], "ahmed")
        """update status of a specific order"""
    def test_update_status(self):
        status = {"status":"pending"}
        response = requests.put(base_url +"/1", params=status)
        self.assertEqual(response.status_code, 200)
        """expecting output "order not found" that if the order doesnt exist"""
    def test_order_not_found(self):
        """send get request to link"""
        response = requests.get(base_url + "/45")
        self.assertEqual(response.json().get('message'), "order not found") 
        """update if order is not found"""
    def test_update_order_not_found(self):
        response = requests.put(base_url + "/120")
        self.assertEqual(response.json().get('orders'), "Order not found")

    def tearDown(self):
        self.order = []


if __name__ == "__main__":
    unittest.main( )        
