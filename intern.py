from flask import Flask, jsonify,request,make_response
import jwt
import datetime
from functools import wraps
import json

app = Flask(name)
app.config['SECRET_KEY']='thisisthesecretkey'

def token_required(f):
	@wraps(f)
def decorated(*args,**kwargs):
	token = request.args.get('token')
	if not token:
	return jsonify({'message':'token is missing'}),403
	try:
	data = jwt.decode(token, app.config['SECRET_KEY'])
	except:
	return jsonify({'message': 'token is invalid'}),403
	return f(*args,**kwargs)
	return decorated
@app.route('/protected')
@token_required

def protected():
return jsonify({
"pan": "ANRPM1729K",
"name": "John",
"dob": "1999-06-11",
"father_name": "Joseph",
"client_id": "4feb601e-2316-4dda-8d91-28c89cdb2335"
})

@app.route('/login')
def login():

auth = request.authorization
if auth and auth.password == "password":
    token = jwt.encode({'user':auth.username ,'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
    return jsonify({'token' : token.decode('UTF-8')})

return make_response('could not verify',401,{'WWW-Authenticate':'Basic realm = "login required"'})
@app.route('/C_id')
def c_id():
return 'c_id addeed'

if name=="main":
