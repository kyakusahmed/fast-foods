import unittest
import json
from app1.models.views import app2
from app1.models.admin import Admin
from app1.models.user import User


class AdminTest(unittest.TestCase):

    def setUp(self):
        self.app1 = app2.test_client()
        self.app1.testing = True
        self.order = {"user_id", "quantity", "location", "status", "created_at"}

    def test_get_all_orders(self):
        response = self.app1.get("/api/v1/orders")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        self.assertIsInstance(data['orders'], list)
    
    def test_place_order(self):
        response = self.app1.post("/api/v1/orders", json=self.order)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        assert data['orders']['user_id'] == "ahmad"
        assert data['orders']['quantity'] == "5kg"
        assert data['orders']['location'] == "kla"
        assert data['orders']['status'] == "pending"
        assert data['orders']['created_at'] == "22/09/2018"
        

    # def test_get_order(self):
    #     self.app1.post('/api/v1/orders', json=self.order)
    #     response = self.app1.get('/api/v1/orders/1')
    #     data = json.loads(response.get_data(as_text=True))
    #     assert data['order'][0]['food_name'] == ""
    #     assert data['order'][0]['userid'] == "ahmad"
    #     assert data['order'][0]['status'] == "pending"
    #     assert response.status_code == 200

    # def test_update_status(self):
    #     self.app.post('/api/v1/orders', json=self.order)
    #     response =self.app.put('/api/v1/orders/1', json={"status": "completed"})
    #     data = json.loads(response.get_data(as_text=True))
    #     assert data['orders'][0]['status'] == "completed"
   
    # def test_order_not_found(self):
    #     response =self.app.get('/api/v1/orders/12345')
    #     data = json.loads(response.get_data(as_text=True))
    #     assert data["message"] == "order not found"
    #     assert response.status_code == 404

    # def test_update_status_not_found(self):
    #     response = self.app.put('/api/v1/orders/4676', json={"status": "completed"})
    #     data = json.loads(response.get_data(as_text=True))
    #     assert data["orders"] == "Order not found"
    #     assert response.status_code == 200
