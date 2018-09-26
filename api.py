from flask import Flask, jsonify, request
from app import Order

app2 = Flask(__name__)
order = Order()

@app2.route('/api/v1/orders', methods=['GET'])
def return_all_orders():
    return jsonify({"orders" : order.return_all_orders()}), 200

@app2.route('/api/v1/orders/<int:id>', methods=['GET'])
def get_order(id):
    search_order = order.get_order(id)
    if search_order:
        return jsonify({"order":search_order}) 
    return jsonify({"message" : "order not found"}), 200

@app2.route('/api/v1/orders', methods=['POST'])
def add_one():
    if not request.args.get("foodid"):
        return jsonify({"error": "Food is required"})
    return jsonify({"orders" : order.add_order(
        request.args.get("foodid"),
        request.args.get("userid"),
        request.args.get("date"),
        request.args.get("status")
        )}), 201

@app2.route('/api/v1/orders/<int:id>', methods=['PUT'])
def update_status(id):
    return jsonify({"orders" : order.update_status(id, request.args.get("status"))})

if __name__ == "__main__":
    app2.run(debug=True, port=8080)