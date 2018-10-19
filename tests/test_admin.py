import json
from .base_tests import BaseTest

class AdminTest(BaseTest):
       
    def test_registration_successful(self):
        data = {
           "first_name":"ahmed",
	       "last_name":"kyakus",
	       "email":"ahmed@outlook.com",
	       "password":"123456",
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
        self.app1.post('/api/v1/users/registration', content_type = "application/json", data=json.dumps(data))
     
        data = {
            "email": "kyakus@outlook.com",
            "password": "123456"
        }
        result = self.app1.post('/api/v1/users/login', content_type = "application/json", data=json.dumps(data))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["msg"], "Login successful")

    def test_invalid_email_login(self):
        data = {
           "first_name":"ahmed",
	       "last_name":"kyakus",
	       "email":"kyakus@outlook.com",
	       "password":"123456",
	       "role": "admin"
           }
        self.app1.post('/api/v1/users/registration', content_type = "application/json", data=json.dumps(data))
     
        data = {
            "email": "@outlook.com",
            "password": "123456"
        }
        result = self.app1.post('/api/v1/users/login', content_type = "application/json", data=json.dumps(data))
        # self.assertEqual(result.status_code, 406)
        self.assertEqual(json.loads(result.data)["msg"], "invalid email")

    def test_role_doesnt_exist(self):
        data = {
           "first_name":"ahmed",
	       "last_name":"kyakus",
	       "email":"kyakus@outlook.com",
	       "password":"123456",
	       "role": "mime"
           }
        response = self.app1.post('/api/v1/users/registration', content_type = "application/json", data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)["error"], " role mime doesnot exist")

    def test_delete_user(self):
        token = self.return_admin_token()
       
        data = {
           "first_name":"ahmd",
	       "last_name":"kyaku",
	       "email":"ahmd@outlook.com",
	       "password":"12a456",
	       "role": "admin"
        }
        self.app1.post('/api/v1/users/registration', content_type="application/json", data=json.dumps(data))

        data = {
            "email":"ahmd@outlook.com",
	        "password":"12a456"
        }
        self.app1.post('/api/v1/users/login', content_type = "application/json", data=json.dumps(data))
        response =  self.app1.delete('/api/v1/users/1', headers={"Authorization": "Bearer " + token})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['msg'], "data deleted")

    def test_get_all_users(self):
        token = self.return_admin_token()
        data = {
           "first_name":"ahmd",
	       "last_name":"kyaku",
	       "email":"ahmd@outlook.com",
	       "password":"12a456",
	       "role": "admin"
        }
        self.app1.post('/api/v1/users/registration', content_type="application/json", data=json.dumps(data))
        data = {
            "email":"ahmd@outlook.com",
	        "password":"12a456"
        }
        self.app1.post('/api/v1/users/login', content_type = "application/json", data=json.dumps(data))
        response = self.app1.get('/api/v1/users', headers={"Authorization": "Bearer " + token})
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data)['users'], list)

    def test_get_all_orders_unauthorised(self):
        response = self.app1.get("/api/v1/orders")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")
    
   
    def test_get_order_without_token(self):
        response = self.app1.get('/api/v1/orders/1')
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")

    def test_update_status_without_token(self):
        response =self.app1.put('/api/v1/orders/1', json={"status": "completed"})
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")

    def test_order_not_found(self):
        response =self.app1.get('/api/v1/orders/12345')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Missing Authorization Header")
        assert response.status_code == 401

    def test_add_food_without_token(self):
        data = {
            "food_title": "burger",
            "food_description": "banns",
            "price":"2000",
            "status":"pending"
        }

        response = self.app1.post('/api/v1/menu',content_type="application/json", data=json.dumps(data))
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['msg'], "Missing Authorization Header")
        assert response.status_code == 401

    def test_get_menu_without_token(self):
        response =self.app1.get('/api/v1/menu')
        data = json.loads(response.get_data(as_text=True)) 
        self.assertEqual(data['msg'], "Missing Authorization Header")
        assert response.status_code == 401

    def test_view_user_history_without_token(self):
        response =self.app1.get('/api/v1/orders')
        data = json.loads(response.get_data(as_text=True)) 
        self.assertEqual(data['msg'], "Missing Authorization Header")
        assert response.status_code == 401
        
    def test_get_orders(self):
        token = self.return_user_token()
        response = self.app1.get("/api/v1/orders", headers={"Authorization":"Bearer " + token})
        data = json.loads(response.get_data())
        assert response.status_code == 401
        self.assertEqual(data['msg'], "unauthorised access")

    def test_get_orders_with_admin_token(self):
        token = self.return_admin_token()
        response = self.app1.get("/api/v1/orders", headers={"Authorization":"Bearer " + token})
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data['orders'], list)            

    

    def test_add_food_to_menu_with_admin_token(self):
        token = self.return_admin_token()
        data = {
            "food_title":"maunches",
            "description":"banns plus creamy biscuits",
            "price":"500k",
            "status":"pending"
            }
        response = self.app1.post("/api/v1/menu", headers={"Authorization": "Bearer " + token}, json=data)
        self.assertEqual(response.status_code, 201)
        assert json.loads(response.data)['menu'] == "Data Inserted Successfully"
    
        # response = self.app1.post("/api/v1/menu", headers={"Authorization": "Bearer " + token}, json=data)
        # self.assertEqual(response.status_code, 201)
        # assert json.loads(response.data)['menu'] == "Data Inserted Successfully"   


    def test_get_menu(self):
        token = self.return_admin_token()
        response = self.app1.get("/api/v1/menu", headers={"Authorization": "Bearer " + token})
        assert response.status_code == 200
        self.assertIsInstance(json.loads(response.data)['menu'], list)

    def test_update_status(self):
        token = self.return_admin_token()
        MENU_DATA = {
            "food_title":"maunches",
            "description":"banns plus creamy biscuits",
            "price":"500k",
            "status":"pending"
            }
        
        self.app1.post(
            '/api/v1/menu',
            headers={"Authorization": "Bearer " + token},
            json=MENU_DATA)

        ORDER_DATA = {
            "user_id": "1",
            "quantity": "12kg",
            "location": "manafa",
            "status": "pending"
            }

        self.app1.post(
            "/api/v1/orders",
            headers={"Authorization": "Bearer " + token}, 
            json=ORDER_DATA)

        response = self.app1.put(
            "/api/v1/orders/1",
            headers={"Authorization": "Bearer " + token},
            json={"status": "Complete"})
        self.assertEqual(response.status_code, 200)
        assert json.loads(response.data)['order'] == "status updated"

    
            







    


     









        
        


  




        





