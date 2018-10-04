from flask import Flask, jsonify, request
from .user import User
from .admin import Admin

from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)


app2 = Flask(__name__)
jwt = JWTManager(app2)
app2.config['JWT_SECRET_KEY'] = 'super-secret'
user = User()
admin = Admin()



@app2.route('/api/v1/users/orders', methods=['POST'])
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
    elif not data.get('created_at'):
        return jsonify({"error":"created_at is required"})
    return jsonify({"orders": user.place_order(
                data["user_id"],
                data["quantity"],
                data["location"],
                data["status"],
                data["created_at"]
                )}), 201    






   











  

if __name__ == "__main__":
    app2.run(debug=True, port=8080)



