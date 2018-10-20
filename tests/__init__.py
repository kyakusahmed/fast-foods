
import random

REGISTER_USER = {
    "first_name":"ahmed",
    "last_name":"kyakus",
    "email":"ahmed@outlook.com",
    "password":"123456",
    "role": "user"
}

REGISTER_ADMIN = {
    "first_name": "Admin",
    "last_name": "Admin",
    "email": "admin@admin.com",
    "password": "adminadmin",
    "role": "admin"
}

REGISTER_USER_RANDOM_EMAIL = {
    "first_name": "Manzede",
    "last_name": "Benard",
    "email":  random.choice("mkahhewu7382h2yw2627hjhgg") +"nzede@gmail.com",
    "password": "manzede"
}

REGISTER_EMAIL_EXISTS = {
    "first_name": "Manzede",
    "last_name": "Benard",
    "email": "manzede@gmail.com",
    "password": "manzede"
}

USER_LOGIN = {
     "email":"ahmed@outlook.com",
    "password":"123456"
}

ADMIN_LOGIN = {
    "email": "admin@admin.com",
    "password": "adminadmin",
}

WRONG_USER_LOGIN = {
    "email": "kyakus@outlook.com",
    "password": "123456"
}

MENU_DATA = {
     "food_title":"maunches",
	 "description":"banns plus creamy biscuits",
	 "price":"500k",
	 "status":"pending"
}

ORDER_DATA = {
   	"user_id": "1",
	"quantity": "12kg",
	"location": "manafa",
	"status": "pending"
}