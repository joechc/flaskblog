from flask import Flask, render_template, url_for, redirect
app = Flask(__name__) 

@app.route('/')
@app.route('/index')
@app.route('/default')
@app.route('/home')
def home(): 
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

if __name__ == '__main__':
	app.run(host="netadminhk2.hk.oracle.com", port=5002, debug=True)
