from flask import Flask, jsonify, request
from app.models.user import User
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)

app2 = Flask(__name__)
jwt = JWTManager(app2)
app2.config['JWT_SECRET_KEY'] = 'super-secret'
user = User()

@app2.route('/api/v1/users/registration', methods=['POST'])
def registration():
    data = request.get_json()
    if not data.get("first_name"):
        return jsonify({"error": "first_name is required"}), 200
    elif not data.get("last_name"):
        return jsonify({"error": "last_name is required"}), 200
    elif not data.get('email'):
        return jsonify({"error": "email is required"}), 200
    elif not data.get('password'):
        return jsonify({"error":"password is required"})
    return jsonify({"orders": user.register_user(
                data["first_name"],
                data["last_name"],
                data["email"],
                data["password"]
                )}), 201

@app2.route('/api/v1/users/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if not email:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    check_user = user.login_user(email, password)
    if not check_user:
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=check_user)
    return jsonify(access_token=access_token), 200

@app2.route('/api/v1/users/partially-protected', methods=['GET'])
@jwt_required
def partially_protected():
    current_user = get_jwt_identity()
    if current_user:
        return jsonify(logged_in_as=current_user), 200
    else:
        return jsonify(loggeed_in_as='anonymous user'), 200


@app2.route('/api/v1/')        


if __name__ == "__main__":
    app2.run(debug=True, port=8080)




