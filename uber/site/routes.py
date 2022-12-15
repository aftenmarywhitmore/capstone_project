from flask import Blueprint, render_template
#from flask_login import login_required
from ..models import uberUser


site = Blueprint('site', __name__, template_folder = 'site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/about_us')
def about_us():
    return render_template('about_us.html')

@site.route('/how_it_works')
def how_it_works():
    return render_template('how_it_works.html')

@site.route('/profile')
#@login_required
def profile():
    return render_template('profile.html')

@site.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')