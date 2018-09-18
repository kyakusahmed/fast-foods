
from flask import Flask, jsonify, request, json

from app import Order

app2 = Flask(__name__)

orders = Order( )
 
@app2.route('/api/v1/orders/<int:id>', methods = ["GET"])
def get_one(id):
    return jsonify({'orders' : orders.get_order(id)}),200
    
         
if __name__ =="__main__":
    app2.run(debug=True,port = 8080)