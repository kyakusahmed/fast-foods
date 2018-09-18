
from flask import Flask, jsonify, request, json

from app import Order

app2 = Flask(__name__)

orders = Order( )
 
@app2.route('/api/v1/orders',methods = ['GET'])
def return_all_orders( ):
   return jsonify({'orders': orders.return_all_orders()}),200



         
if __name__ =="__main__":
    app2.run(debug=True,port = 8080)