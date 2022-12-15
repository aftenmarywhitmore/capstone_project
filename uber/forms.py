from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class uberUserLoginForm(FlaskForm):
    full_name = StringField('Full Name')
    user_name = StringField('Username')
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField() 

class uberEmployeeForm(FlaskForm): 
    full_name = StringField('Full Name')
    user_name = StringField('Username')
    email = StringField('Email')
    phone_num = StringField('Phone Number')
    address = StringField('Address')
    birthday = StringField('Birthday')
    ref_name = StringField('Reference Name(s)')
    ref_phone = StringField('Reference Phone Number(s)')
    ref_email = StringField('Reference Email(s)')
    today_date = StringField('Todays Date')
    submit_button = SubmitField() 

class uberCustomerForm(FlaskForm): 
    full_name = StringField('Full Name')
    email = StringField('Email')
    phone_num = StringField('Phone Number')
    num_beds = StringField('Number of Bedrooms')
    num_bath = StringField('Number of Bathrooms')
    sqft = StringField('Residence/Office Square Footage')
    req_date = StringField('Requested Clean Date')
    req_time = StringField('Requested Clean Time')
    submit_button = SubmitField() 