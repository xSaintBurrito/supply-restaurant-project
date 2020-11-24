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

#Not correct
#@app.route("/UpdateStudent/<id>",methods=['GET'])
#def updateStudent(id):
  
#    try:
#      sql = "SELECT * FROM studentslesson1 WHERE id=%s"
#      mycursor.execute(sql, id)
#      mydb.commit()
#    except:
#       return jsonify({"Error":status.HTTP_404_NOT_FOUND}), status.HTTP_404_NOT_FOUND
      
  #Arreglar este error
  #  if('id' in myresult):
  
   #   sql = "UPDATE studentslesson1 SET name = %s WHERE id = %s"
   #   val = (request.json['name'],id)
   #   mycursor.execute(sql, val)
   #   mydb.commit()
   #   mycursor.execute("SELECT * FROM studentslesson1")
   #   myresult = mycursor.fetchall()
   #   return jsonify({"student":myresult})
    
   # else:
   #   return jsonify({"Error":status.HTTP_404_NOT_FOUND}), status.HTTP_404_NOT_FOUND

  
    


if __name__ == "__main__" : 
    app.run()

mydb.close()