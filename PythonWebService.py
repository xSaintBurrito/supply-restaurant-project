from flask import Flask
from flask import jsonify
from flask_api import status
from flask import request
app = Flask(__name__)

studentDB = [
    {
        'id' : '11',
        'name' : 'Sergio',
        'section' : 'A'

    },{
        'id' : '12',
        'name' : 'Miguel',
        'section' : 'B'
    }
]

@app.route("/",methods = ['GET'])
def welcome() :
    return "Welcome to Python Webservice" 

@app.route("/students/getStudents", methods = ['GET'])
def getStudents() :
    return jsonify({"stud" : studentDB})

@app.route("/students/getStudent/<id>", methods = ['GET'])
def getStudentDetails(id) :
    student = [stud for stud in studentDB if(stud['id']==id)]
    
    if student:
        return jsonify({"stud" : student}) 
    else:
        
        return jsonify({"Error":status.HTTP_404_NOT_FOUND}), status.HTTP_404_NOT_FOUND
    
@app.route("/students/updateStudent/<id>", methods = ['PUT'])
def updateStudentDetail(id) : 
    student = [stud for stud in studentDB if(stud['id']==id)]

    if ('id' in request.json) : 
        print("Student Aviable")
    if ('name' in request.json) :
        student [0]['name']=request.json['name']
    return jsonify({"stud":student[0]})

@app.route("/students/addStudent", methods = ['POST'])
def addStudent() : 
    student = {
        'id' : request.json['id'],
        'name' : request.json['name'],
        'section' : request.json['section']
    }
    studentDB.append(student)
    return jsonify({"stud":studentDB})
    
@app.route("/students/removeStudent/<id>", methods = ['DELETE'])
def removeStudent(id) : 
    student = [stud for stud in studentDB if(stud['id']==id)]
    if(len(student) > 0) :
        studentDB.remove(student[0])
    return jsonify({"stud":studentDB})

if __name__ == "__main__" : 
    app.run()