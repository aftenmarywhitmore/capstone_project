from datetime import datetime 
from flask_login import UserMixin, LoginManager
from flask_migrate import Migrate 
from flask_marshmallow import Marshmallow 
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash 


import secrets 
import uuid

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow() 

@login_manager.user_loader
def load_user(user_id): 
    return uberUser.query.get(user_id)

#SIGN IN INFO FOR A USER 
class uberUser(db.Model, UserMixin): 
    id = db.Column(db.String, primary_key = True)
    full_name = db.Column(db.String(200), nullable = True, default = 'Full Name')
    user_name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, full_name, user_name, email, password = '', id = '', token = '', g_auth_verify = False):
        self.id = self.set_id()
        self.full_name = full_name
        self.user_name = user_name
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
            return secrets.token_hex(length)
        
    def set_id(self):
            return str(uuid.uuid4()) 

    def set_password(self, password):
            self.pw_hash = generate_password_hash(password)
            return self.pw_hash 

    def __repr__(self):
            return f"User {self.full_name} has been added to the database!" 

#FORM INFO FOR AN EMPLOYEE 
class uberEmployee(db.Model, UserMixin): 
    id = db.Column(db.String, primary_key = True)
    full_name = db.Column(db.String(200))
    user_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone_num = db.Column(db.String(50))
    address = db.Column(db.String(200))
    birthday = db.Column(db.String(50))
    ref_name = db.Column(db.String(200))
    ref_phone = db.Column(db.String(200))
    ref_email = db.Column(db.String(200))
    today_date = db.Column(db.String(50))

    def __init__(self, full_name, user_name, email, phone_num, address, birthday, ref_name, ref_phone, ref_email, today_date):
        self.id = self.set_id()
        self.full_name = full_name
        self.user_name = user_name 
        self.email = email
        self.phone_num = phone_num
        self.address = address
        self.birthday = birthday
        self.ref_name = ref_name
        self.ref_phone = ref_phone
        self.ref_email = ref_email 
        self.today_date = today_date

    def set_token(self, length):
            return secrets.token_hex(length)
        
    def set_id(self):
            return str(uuid.uuid4()) 

    def set_password(self, password):
            self.pw_hash = generate_password_hash(password)
            return self.pw_hash 

    def __repr__(self):
        return f"An application for {self.full_name} has been submitted!"


#CUSTOMER FORM
class uberCustomer(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    full_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone_num = db.Column(db.String(200))
    num_beds = db.Column(db.Numeric(precision = 20, scale = 2))
    num_bath = db.Column(db.Numeric(precision = 20, scale = 2))
    sqft = db.Column(db.Numeric(precision = 10, scale = 4))
    req_date = db.Column(db.String(50))
    req_time = db.Column(db.String(50))

    def __init__(self, full_name, email, phone_num, num_beds, num_bath, sqft, req_date, req_time):
        self.id = self.set_id()
        self.full_name = full_name
        self.email = email
        self.phone_num = phone_num
        self.num_beds = num_beds
        self.num_bath = num_bath
        self.sqft = sqft
        self.req_date = req_date
        self.req_time = req_time

    def set_id(self):
            return str(uuid.uuid4()) 

    def __repr__(self):
        return f"A request for {self.full_name} has been submitted and sent to {self.email}! Please check your email for your confirmation information."


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ['id', 'full_name', 'user_name', 'email', 'phone_num', 'address', 'birthday', 'ref_name', 'ref_phone', 'ref_email', 'today_date']


employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many = True)


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ['id', 'full_name', 'email', 'phone_num', 'num_beds', 'num_bath', 'sqft', 'req_date', 'req_time']


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many = True)