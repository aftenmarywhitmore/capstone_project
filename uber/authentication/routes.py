from flask import Blueprint, render_template, request, redirect, url_for, flash
from uber.forms import uberUserLoginForm, uberEmployeeForm, uberCustomerForm
from uber.models import CustomerSchema, db, uberUser, uberEmployee, uberCustomer
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required 

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

#SIGNUP
@auth.route('/signup', methods = ['GET', 'POST'])
#GET: checking to see if data exists
def signup(): 
    form = uberUserLoginForm()
    try: 
        if request.method == 'POST' and form.validate_on_submit(): 
            full_name = form.full_name.data
            user_name = form.user_name.data
            email = form.email.data
            password = form.password.data
            user = uberUser(full_name, user_name, email, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f'Congrats {full_name}, you have successfully created an account!')

            return redirect(url_for('auth.login'))
    except: 
        raise Exception('Invalid Entry. Please Try Again.')
    return render_template('signup.html', form = form) 

#LOGIN
@auth.route('/login', methods = ['GET', 'POST'])
#GET: checking to match up data in database 
def login(): 
    form = uberUserLoginForm()

    try: 
        if request.method == 'POST' and form.validate_on_submit(): 
            full_name = form.full_name.data
            user_name = form.user_name.data
            email = form.email.data
            password = form.password.data
            print(email, password)

            logged_user = uberUser.query.filter(uberUser.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password): 
                login_user(logged_user)
                flash('Successful Email/Password Login!')
                return redirect(url_for('site.profile'))
            else: 
                flash('Invalid Email/Password', 'auth-failed')
                return redirect(url_for('auth.login'))
    except: 
        raise Exception('Invalid Entry. Please Try Again.')

    return render_template('login.html', form = form)

#LOGOUT 
@auth.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('site.home'))



#EMPLOYEE APPLICATION
@auth.route('/apply', methods = ['POST', 'GET'])

def apply():
    form = uberEmployeeForm()
    try: 
        if request.method == 'POST' and form.validate_on_submit():
            full_name = form.full_name.data
            print(full_name)
            user_name = form.user_name.data
            print(user_name)
            email = form.email.data
            print(email)
            phone_num = form.phone_num.data
            print(phone_num)
            address = form.address.data
            print(address)
            birthday = form.birthday.data
            print(birthday)
            ref_name = form.ref_name.data
            print(ref_name)
            ref_phone = form.ref_phone.data
            print(ref_phone)
            ref_email = form.ref_email.data
            print(ref_email)
            today_date = form.today_date.data
            print(today_date)
            employee = uberEmployee(full_name, user_name, email, phone_num, address, birthday, ref_name, ref_phone, ref_email, today_date)

            db.session.add(employee)
            db.session.commit()

            flash(f'Congrats {full_name}, you have successfully submitted an application!')

            return redirect(url_for('site.thank_you'))
    except: 
        raise Exception('Invalid Entry. Please Try Again.')
    return render_template('apply.html', form = form) 

#CUSTOMER REQUEST 

@auth.route('/cust_request', methods = ['POST', 'GET'])

def cust_request():
    form = uberCustomerForm()
    try: 
        if request.method == 'POST' and form.validate_on_submit(): 
            full_name = form.full_name.data
            print(full_name)
            email = form.email.data
            print(email)
            phone_num = form.phone_num.data
            print(phone_num)
            num_beds = form.num_beds.data
            print(num_beds)
            num_bath = form.num_bath.data
            print(num_bath)
            sqft = form.sqft.data
            print(sqft)
            req_date = form.req_date.data
            print(req_date)
            req_time = form.req_time.data
            print(req_time)
            customer = uberCustomer(full_name, email, phone_num, num_beds, num_bath, sqft, req_date, req_time)

            db.session.add(customer)
            db.session.commit()

            flash(f'Congrats {full_name}, you have successfully submitted an application!')

            return redirect(url_for('site.thank_you'))
    except: 
        raise Exception('Invalid Entry. Please Try Again.')
    return render_template('request.html', form = form) 