from flask import Flask, jsonify, request
from .user import User
from .admin import Admin

from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)


app2 = Flask(__name__)
jwt = JWTManager(app2)
app2.config['JWT_SECRET_KEY'] = 'super-secret'
user = User()
admin = Admin()




@app2.route('/api/v1/orders', methods=["GET"])
@jwt_required
def get_orders():
    current_user = get_jwt_identity()
    if current_user[5] != "admin":
        return jsonify({"msg":"unauthorised access"}), 401
    else:    
        return jsonify({"orders": admin.get_all_orders()})



                       





   

if __name__ == "__main__":
    app2.run(debug=True, port=8080)



