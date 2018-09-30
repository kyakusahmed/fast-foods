import unittest
import json
from app.api import app2

class OrderTest(unittest.TestCase):

    def setUp(self):
        self.app = app2.test_client()
        self.app.testing = True
        self.order = {"food_name": "ahmad", "userid": 5, "status": "pending"}

    def test_get_all_orders(self):
        response = self.app.get("/api/v1/orders")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        self.assertIsInstance(data['orders'], list)
    
    def test_add_order(self):
        response = self.app.post("/api/v1/orders", json=self.order)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        assert data['orders']['food_name'] == "ahmad"
        assert data['orders']['userid'] == 5
        assert data['orders']['status'] == "pending"

    def test_get_order(self):
        self.app.post('/api/v1/orders', json=self.order)
        response = self.app.get('/api/v1/orders/1')
        data = json.loads(response.get_data(as_text=True))
        assert data['order'][0]['food_name'] == "ahmad"
        assert data['order'][0]['userid'] == 5
        assert data['order'][0]['status'] == "pending"
        assert response.status_code == 200

    def test_update_status(self):
        self.app.post('/api/v1/orders', json=self.order)
        response =self.app.put('/api/v1/orders/1', json={"status": "completed"})
        data = json.loads(response.get_data(as_text=True))
        assert data['orders'][0]['status'] == "completed"
   
    def test_order_not_found(self):
        response =self.app.get('/api/v1/orders/12345')
        data = json.loads(response.get_data(as_text=True))
        assert data["message"] == "order not found"
        assert response.status_code == 404

    def test_update_status_not_found(self):
        response = self.app.put('/api/v1/orders/4676', json={"status": "completed"})
        data = json.loads(response.get_data(as_text=True))
        assert data["orders"] == "Order not found"
        assert response.status_code == 200


        


    

    




