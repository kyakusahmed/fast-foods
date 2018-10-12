from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
from .user import User
from .admin import Admin
from re import match
import datetime

from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity,jwt_optional)


app2 = Flask(__name__)
Swagger(app2)
jwt = JWTManager(app2)
app2.config['JWT_SECRET_KEY'] = 'super-secret'
user = User()
admin = Admin()


@app2.route('/api/v1/users/registration', methods=['POST'])
@swag_from("../docs/signup&signin/signup.yaml")
def registration():
    data = request.get_json()
    required = ("first_name", "last_name", 'email', 'password', 'role')
    if not set(required).issubset(set(data)):
        return jsonify({"error": "some fields are missing"}), 200
    if not bool(
            match(
                r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
                data["email"])):
        return jsonify({"msg":"invalid email"}), 406

    if len(data["password"]) < 5:
        return jsonify({"msg":"passowrd is too short"}), 406
    
    user_role = data['role']
    user_roles = ['admin', 'user']
    if user_role not in user_roles:
        return jsonify({"error": " role {} doesnot exist".format(user_role)}), 200

    return jsonify({"msg": user.register_user(
                data["first_name"],
                data["last_name"],
                data["email"],
                data["password"],
                data["role"]
                )}), 201

@app2.route('/api/v1/users/login', methods=['POST'])
@swag_from("../docs/signup&signin/signin.yaml")
def login():
    data = request.get_json()
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    
    if not bool(
            match(
                r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",
                data["email"])):
        return jsonify({"msg":"invalid email"}), 406

    if len(data["password"]) < 5:
        return jsonify({"msg":"passowrd is too short"}), 406 
    check_user = user.login_user(email, password)
    print(check_user)
    if not check_user:
        return jsonify({"msg":"register first"}), 406
    access_token = create_access_token(identity=check_user)
    return jsonify(access_token=access_token, msg="Login successful"), 200



@app2.route('/api/v1/users/orders', methods=['POST'])
@swag_from("../docs/orders/place_order.yaml")
@jwt_required
def place_order():
    data = request.get_json()
    if not data.get("user_id"):
        return jsonify({"error": "user_id is required"}), 200
    elif not data.get("quantity"):
        return jsonify({"error": "quantity is required"}), 200
    elif not data.get('location'):
        return jsonify({"error": "location is required"}), 200
    elif not data.get('status'):
        return jsonify({"error":"status is required"})

    return jsonify({"orders": user.place_order(
                data["user_id"],
                data["quantity"],
                data["location"],
                data["status"],
                datetime.datetime.now()
                )}), 201    

@app2.route('/api/v1/users/orders/<user_id>', methods=['GET'])
@jwt_required
def view_user_history(user_id):
    if not user_id:
        return jsonify({"msg":"user_id not found"})
    else:
        orders = user.view_user_history(user_id)
        new_list = []
        for key in range(len(orders)):
            new_list.append({   
                    'orders_id':orders[key][0],
                    'user_id':orders[key][1],
                    'quantity':orders[key][2],
                    'location':orders[key][3],
                    'status':orders[key][4]
                }

            )
    return jsonify({"orders": new_list})

@app2.route('/api/v1/orders', methods=["GET"])
@jwt_required
def get_orders():
    current_user = get_jwt_identity()
    if current_user[5] != "admin":
        return jsonify({"msg":"unauthorised access"}), 401
    else:    
        return jsonify({"orders": admin.get_all_orders()})



@app2.route('/api/v1/orders/<int:orders_id>', methods=["GET"])
@jwt_required
def get_order(orders_id):
    current_user = get_jwt_identity()
    if current_user[5] != "admin":
        return jsonify({"msg":"unauthorised access"}), 401
    else:
        order = Admin().get_one_order(orders_id)
        return jsonify({"order": {   
                    'orders_id':order[0],
                    'user_id':order[1],
                    'quantity':order[2],
                    'location':order[3],
                    'status':order[4]
                }}), 200


@app2.route('/api/v1/orders/<int:orders_id>', methods=["PUT"])
@jwt_required
def update_status(orders_id):
    current_user = get_jwt_identity()
    if current_user[5] != "admin":
        return jsonify({"msg":"unauthorised access"}), 401
    else:
        get_input = request.get_json()
        if not get_input.get("status"):
            return jsonify({"error" : "status is required"}), 200
        return jsonify({"orders" : admin.update_order_status(orders_id, get_input["status"])}), 200


@app2.route('/api/v1/menu', methods=["GET"])
@jwt_required
def get_menu():
    menu = admin.get_menu()
    new_list = []
    for key in range(len(menu)):
        new_list.append(
            {   
                'menu_id':menu[key][0],
                'food_title':menu[key][1],
                'description':menu[key][2],
                'price':menu[key][3],
                'status':menu[key][4]
            }

        )
    return jsonify({"menu":new_list}), 200   

@app2.route('/api/v1/menu', methods=["POST"])
@jwt_required
def add_food_to_menu():
    current_user = get_jwt_identity()
    print(current_user[5])
    if current_user[5] != "admin":
        return jsonify({"msg":"unauthorised access"}), 401
    else:
        data = request.get_json()
        if not data.get("food_title"):
            return jsonify({"error": "food_title is required"}), 200
        elif not data.get("description"):
            return jsonify({"error": "description is required"}), 200
        elif not data.get('price'):
            return jsonify({"error": "price is required"}), 200
        elif not data.get('status'):
            return jsonify({"error":"status is required"})
        return jsonify({"menu":admin.add_meal(
                    data["food_title"],
                    data["description"],
                    data["price"],
                    data["status"]
                    )}), 201    


@app2.route('/api/v1/partially-protected', methods=['GET'])
@jwt_optional
def partially_protected():
    current_user = get_jwt_identity()
    if current_user:
        return jsonify(logged_in_as=current_user), 200
    else:
        return jsonify(loggeed_in_as='anonymous user'), 200
                 

if __name__ == "__main__":
    app2.run(debug=True, port=8080)



