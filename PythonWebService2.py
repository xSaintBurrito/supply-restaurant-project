from flask import Flask
from flask import jsonify
from flask_api import status
from flask import request
import pymysql
import mysql.connector
import sys

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database ="students"
)

mycursor = mydb.cursor()

   
@app.route("/",methods = ['GET'])
def welcome() :
  mycursor.execute("SELECT * FROM studentslesson1")
  myresult = mycursor.fetchall()
  print(myresult)
  return jsonify({"student":myresult})

@app.route("/AddStudent",methods = ['POST'])
def addStudent() : 
 
  sql = "INSERT INTO studentslesson1 (id, name, section) VALUES (%s, %s, %s)"
  val = (request.json['id'], request.json['name'],request.json['section'])
  
  mycursor.execute(sql, val)
  mydb.commit()
  mycursor.execute("SELECT * FROM studentslesson1")
  myresult = mycursor.fetchall()
  return jsonify({"student":myresult})


if __name__ == "__main__" : 
    app.run(host='0.0.0.0')

mydb.close()