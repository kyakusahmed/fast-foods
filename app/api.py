from flask import Flask, jsonify, request
from app.manage import Order

app2 = Flask(__name__)
order = Order()

@app2.route('/api/v1/orders', methods=['GET'])
def return_all_orders():
    return jsonify({"orders" : order.return_all_orders()}), 200

@app2.route('/api/v1/orders/<int:id>', methods=['GET'])
def get_order(id):
    search_order = order.get_order(id)
    if search_order:
        return jsonify({"order":search_order}), 200
    return jsonify({"message" : "order not found"}), 404

@app2.route('/api/v1/orders', methods=['POST'])
def add_one():
    data = request.get_json()
    if not data.get("food_name"):
        return jsonify({"error": "food_name is required"}), 200
    elif not data.get("userid"):
        return jsonify({"error": "userid is required"}), 200
    elif not data.get('status'):
        return jsonify({"error": "status is required"}), 200
    return jsonify({"orders": order.add_order(
                data["food_name"],
                data["userid"],
                data["status"]
            )}), 201

@app2.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_status(id):
    get_input = request.get_json()
    if not get_input.get("status"):
        return jsonify({"error" : "status is required"}), 200
    return jsonify({"orders" : order.update_status(id, get_input["status"])}), 200

    
