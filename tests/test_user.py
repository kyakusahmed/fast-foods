import json
from .base_tests import BaseTest

class UserTest(BaseTest):
    
    def test_registration_successful(self):
        data = {
           "first_name":"yusuf",
	       "last_name":"kyakus",
	       "email":"yusuf@gmail.com",
	       "password":"123abc",
	       "role": "user"
        }
        response = self.app1.post('/api/v1/users/registration', content_type="application/json", data=json.dumps(data))
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        data = {
           "first_name":"yusuf",
	       "last_name":"kyakus",
	       "email":"yusuf@gmail.com",
	       "password":"123abc",
	       "role": "user"
           }
        self.app1.post('/api/v1/users/registration', content_type = "application/json", data=json.dumps(data))
     
        data = {
            "email":"yusuf@gmail.com",
	        "password":"123abc",
        }
        result = self.app1.post('/api/v1/users/login', content_type = "application/json", data=json.dumps(data))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["msg"], "Login successful")

    def test_place_order_without_token(self):
        response = self.app1.post("/api/v1/users/orders")
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 401
        self.assertEqual(data['msg'], "Missing Authorization Header")

    def test_get_order_with_user_token(self):
        token = self.return_user_token() 
        response = self.app1.get('/api/v1/orders/1', headers={"Authorization":"Bearer " + token})
        data = json.loads(response.get_data())
        assert response.status_code == 401
        self.assertEqual(data['msg'], "unauthorised access")

    def test_view_user_history(self):
        token = self.return_user_token() 
        response =self.app1.get('/api/v1/menu', headers={"Authorization":"Bearer " + token}) 
        assert response.status_code == 200
        
          

    def test_add_food_to_menu_user_token(self):
        token = self.return_user_token()
        data = {
            "food_title":"maunches",
            "description":"banns plus creamy biscuits",
            "price":"500k",
            "status":"pending"
            }
        response = self.app1.post("/api/v1/menu", headers={"Authorization": "Bearer " + token},json=data)
        self.assertEqual(response.status_code, 401)
        assert json.loads(response.data)['msg'] == "unauthorised access"
    

    
    def test_place_order(self):

        admin_token = self.return_admin_token()

        data1 = {
            "food_title":"maunches",
            "description":"banns plus creamy biscuits",
            "price":"500k",
            "status":"pending"
            }
        self.app1.post('/api/v1/menu', headers={"Authorization": "Bearer " + admin_token},
            json=data1)

        token = self.return_user_token()

        data2 = {
            "food_title":"maunches",
            "description":"banns plus creamy biscuits",
            "price":"500k",
            "status":"pending"
            }
        response = self.app1.post('/api/v1/users/orders', headers={"Authorization":"Bearer " + token}, json=data2)
        assert response.status_code == 200
        # assert json.loads(response.data)['menu'] == "Data Inserted Successfully"

        # admin_token = self.return_admin_token()
        # data = {
        #     "food_title":"maunches",
        #     "description":"banns plus creamy biscuits",
        #     "price":"500k",
        #     "status":"pending"
        #     }
        # self.app1.post('/api/v1/menu', headers={"Authorization": "Bearer " + admin_token}, json=data)
        # token = self.return_user_token()
        # data1 = {
        #     "user_id": "1",
        #     "quantity": "12kg",
        #     "location": "manafa",
        #     "status": "pending"
        #     }
        # response =  self.app1.post('/api/v1/users/orders', headers={"Authorization": "Bearer " + token}, json=data1)
        # self.assertEqual(response.status_code, 201)
        # assert json.loads(response.data1)['menu'] == "Data Inserted Successfully"
        
    
        
