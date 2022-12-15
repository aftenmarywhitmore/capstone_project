#API ROUTES.PY --> IMPORT token_required FROM uber.helpers 
#MODELS.PY --> create uberUser class for import 

from functools import wraps 
from flask import request, jsonify, json 
from uber.models import uberUser 

import secrets 
import decimal 

def token_required(our_flask_function): 
    @wraps(our_flask_function)
    def decorated(*args, **kwargs): 
        token = None 
    
        if 'x-access-token' in request.headers: 
            token = request.headers['x-access-token'].split(' ')[1]
            print(token)

        if not token: 
            return jsonify({'message' : 'Token Does Not Exist'}), 401
        
        try: 
            current_user_token = uberUser.query.filter_by(token = token).first()
            print(current_user_token)
            if not current_user_token or current_user_token.token != token: 
                return jsonify({ 'message' : 'Not a Valid Token'})
        
        except: 
            owner = uberUser.query.filter_by(token = token).first()
            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message' : 'Not a Valid Token'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)



