from flask import Flask, render_template,request,url_for
import authorize as a
import verify_user as vu


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def Home():
    return render_template('user_info.html')
@app.route('/success',methods=['POST'])
def success():
	 username=request.form['username']
	 device_id=request.form['device_id']
	 user_hash=request.form['hash']
	 user_info=[username,device_id,user_hash]
	 if vu.get_user_verified(user_info):
	 	return render_template('verified.html',  name=username ,device=device_id)
	 else:
	 	return 'you are not registered'
@app.route('/registered',methods=['GET','POST'])
def registered_user():
	return render_template('registered.html')
	
@app.route('/user_register',methods=['POST'])
def new_user():
	username = request.form['username']
	device_id = request.form['device_id']
	user_info = [username,device_id]
	if a.authorization_done(user_info):
		user_hash = a.secret_hash[0]
		a.secret_hash.clear()
		return render_template('user_register.html' , name=username,secret=user_hash)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=4006)
