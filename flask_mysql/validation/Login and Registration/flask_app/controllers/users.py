from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session

app.secret_key = "474674sdf"

# return the Login and Register page
@app.route('/')
def login_registration():
    return render_template('index.html')



#get the info from the registration form form
@app.route('/register', methods=['POST'])
def register():
    data = request.form

    if User.validate_register(data):
        User.create(data)
        pass

    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    data = request.form
    print(data)
    if User.validate_login(data):
        session['logged_user_email'] = data['email']
        print(session['logged_user_email'])
        return redirect('/dashboard')
    return redirect('/')


@app.route('/dashboard')
def dashboard():
    logged_user = User.get_by_email({'email': session['logged_user_email']})
    # This route will return the dashboard page after the user successfully logs in.
    return render_template('dashboard.html', logged_user=logged_user)


@app.route('/logout', methods=['POST'])
def logout():
    print('logoutttttttttttttttttt')
    session.clear()  
    return redirect('/')
