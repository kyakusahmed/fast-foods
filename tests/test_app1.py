import unittest
import json
from app1.models.views import app2

class AdminTest(unittest.TestCase):

    def setUp(self):
        self.app1 = app2.test_client()
        self.app1.testing = True
       
    def test_registration_successful(self):
        data = {
           "first_name":"ahmed",
	       "last_name":"kyakus",
	       "email":"ahmed@outlook.com",
	       "password":"1234",
	       "role": "admin"
        }
        response = self.app1.post('/api/v1/users/registration', content_type="application/json", data=json.dumps(data))
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        data = {
           "first_name":"ahmed",
	       "last_name":"kyakus",
	       "email":"kyakus@outlook.com",
	       "password":"123456",
	       "role": "admin"
           }
        self.app1.post('/api/v1/users/registration', content_type="application/json", data=json.dumps(data))
     
        data = {
            "email": "kyakus@outlook.com",
            "password": "123456"
        }
        result = self.app1.post('/api/v1/users/login', content_type="application/json", data=json.dumps(data))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["msg"], "Login successful")
        

    def test_get_all_orders_unauthorised(self):
        response = self.app1.get("/api/v1/orders")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")
    
    def test_place_order(self):
    
        response = self.app1.post("/api/v1/users/orders")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")
        
    def test_get_order(self):
        response = self.app1.get('/api/v1/orders/1')
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")


    def test_update_status(self):
        response =self.app1.put('/api/v1/orders/1', json={"status": "completed"})
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")

        
   
    def test_order_not_found(self):
        response =self.app1.get('/api/v1/orders/12345')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Missing Authorization Header")
        assert response.status_code == 401

    def test_update_status_not_found(self):
        response = self.app1.put('/api/v1/orders')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Missing Authorization Header")
        assert response.status_code == 401
