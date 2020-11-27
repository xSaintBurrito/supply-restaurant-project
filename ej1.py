import sys
from flask import Flask
from flask import jsonify
from flask_api import status
from flask import request
import pymysql
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database ="delivery"
)

mycursor = mydb.cursor()

   
@app.route("/",methods = ['GET'])
def welcome() :
    mycursor.execute("SELECT * FROM orders")
    myresult = mycursor.fetchall()
    print(myresult)
    return jsonify({"order":myresult})

@app.route("/AddOrder",methods = ['POST'])
def addOrder() : 
 
    sql = "INSERT INTO orders (id, product, prize) VALUES (%s, %s, %s)"
    val = (request.json['id'], request.json['product'],request.json['prize'])
  
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("SELECT * FROM orders")
    myresult = mycursor.fetchall()
    return jsonify({"order":myresult})

@app.route("/DeleteOrder",methods = ['DELETE'])
def deleteOrder(id):
    sql = "DELETE FROM orders WHERE id == value"
    val = (request.json['id'], request.json['product'],request.json['prize'])
  
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("SELECT * FROM orders")
    myresult = mycursor.fetchall()
    return jsonify({"order":myresult})

#select rider 

#payment 

@app.route("/PayOrder",methods = ['POST'])
def payOrder(id): 
    sql = "INSERT INTO payments (id, cardinfo, prize) VALUES (%s, %s, %s)"
    val = (request.json['id'], request.json['cardinfo'],request.json['prize'])
  
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.execute("SELECT * FROM payments")
    myresult = mycursor.fetchall()
    return jsonify({"payment order":myresult})



#Not correct
#@app.route("/UpdateOrder/<id>",methods=['PUT'])
#def updateStudent(id):
#    try:
#      sql = "SELECT * FROM orders WHERE id=%s"
#      mycursor.execute(sql, id)
#      mydb.commit()
#    except:
#       return jsonify({"Error":status.HTTP_404_NOT_FOUND}), status.HTTP_404_NOT_FOUND
      
  #Arreglar este error
  #  if('id' in myresult):
  
   #   sql = "UPDATE orders SET product = %s WHERE id = %s"
   #   val = (request.json['product'],id)
   #   mycursor.execute(sql, val)
   #   mydb.commit()
   #   mycursor.execute("SELECT * FROM orders")
   #   myresult = mycursor.fetchall()
   #   return jsonify({"order":myresult})
    
   # else:
   #   return jsonify({"Error":status.HTTP_404_NOT_FOUND}), status.HTTP_404_NOT_FOUND

  
    


if __name__ == "__main__" : 
    app.run()

mydb.close()