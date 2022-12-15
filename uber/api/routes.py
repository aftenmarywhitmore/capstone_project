#API for EMPLOYEE APPLICATION & CUSTOMER REQUEST FORM

from flask import Blueprint, request, jsonify
from uber.tools import token_required 
from uber.models import db, uberUser, employee_schema, employees_schema, customer_schema, customers_schema

api = Blueprint('api', __name__, url_prefix = '/api')


#EMPLOYEE APPLICATION
#how to post emp apps (drone inventory/kardash inventory - swap column names) 
@api.route('/application', methods = ['POST']) #POST needs to match http request in insomnia: 
@token_required
def create_application(current_user_token):
    full_name = request.json['full_name']
    user_name = request.json['user_name']
    email = request.json['email']
    phone_num = request.json['phone_num']
    address = request.json['address']
    birthday = request.json['birthday']
    ref_name = request.json['ref_name']
    ref_phone = request.json['ref_phone']
    ref_email = request.json['ref_email']
    today_date = request.json['today_date']
    user_token = current_user_token.token

    print(f'User Token: {current_user_token.token}')

    employee = uberUser(full_name, user_name, email, phone_num, address, birthday, ref_name, ref_phone, ref_email, today_date, user_token = user_token)

    db.session.add(employee)
    db.session.commit()

    response = employee_schema.dump(employee) 

    return jsonify(response) 
    

#CUSTOMER REQUEST FORM
@api.route('/request', methods = ['POST'])
@token_required 
def create_request(current_user_token):
    full_name = request.json['full_name']
    email = request.json['email']
    phone_num = request.json['phone_num']
    num_beds = request.json['num_beds']
    num_bath = request.json['num_bath']
    sqft = request.json['sqft']
    req_date = request.json['req_date']
    req_time = request.json['req_time']
    user_token = current_user_token.token

    print(f'User Token')

    customer = uberUser(full_name, email, phone_num, num_beds, num_bath, sqft, req_date, req_time, user_token = user_token)

    db.session.add(customer)
    db.session.commit()

    response = customer_schema.dump(customer) 

    return jsonify(response) 
