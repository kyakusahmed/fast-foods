
from flask import Flask, jsonify, request, json

from app import Order

app2 = Flask(__name__)

orders = Order( )
 

@app2.route('/api/v1/orders',methods = ['POST'])
def addone():
    data = request.get_json()
    id = data["id"]
    foodid = data["foodid"]
    userid = data["userid"]
    date = data["date"]
    status = data["status"]
    return jsonify({'orders' : orders.add_order(id, foodid, userid, date, status)}),201
    
    
         
if __name__ =="__main__":
    app2.run(debug=True,port = 8080)