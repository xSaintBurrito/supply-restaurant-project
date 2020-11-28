from flask_restful import request, Resource
from wtforms import Form, validators, StringField, PasswordField

class NewUserForm(Form): 
    user = StringField("Username: ", [validators.DataRequired()])
    password = PasswordField("Password: ", [validators.DataRequired()])

class NewUser(Resource): 
    def post(self): 
        form = NewUserForm(request.form)
        if not form.validate(): 
            return "not valid", 400
        else:
             return "ok", 200


