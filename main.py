from flask import Flask, render_template, request, url_for, redirect
from model import User, Post, Comment
from sqlalchemy.orm import Session
from connection import engine

app = Flask(__name__)

session = Session(bind=engine)

@app.route('/')
def feed():
    return render_template('index.html')

# @app.route('/User/<name>')
# def get_user(name):
#     return render_template('one_user.html', user_name=name)

#region Show and create Post

@app.route('/post/', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']

        # INSERT INTO DATABASE WITH TRY EXCEPT

        return redirect('/') # Do not forget to update
    else:
        return render_template('post.html')

#endregion

#region Register and Log In

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # CHECK IF USER EXISTS INTO DATABASE
        user = session.query(User).filter_by(username=username, password=password).scalar()
        
        if user != None:
            return redirect(url_for('success', name=username))
        else:
            return {"error": "Username or password does not match or exist."}
    else:
        return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}'

@app.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Refuse the guest to register if duplicate username or email.
        duplicate_email = session.query(User).filter_by(email=email).scalar()
        duplicate_username = session.query(User).filter_by(username=username).scalar()
        if duplicate_email != None or duplicate_username != None:
            return {"error": "user already exist"}

        new_user = User(
            username= username,
            email = email,
            password = password
        )
        # INSERT INTO DATABASE
        try:
            session.add(new_user)
            session.commit()
            return redirect(url_for('login'))
        except:
            return {"error": "There was an issue to register your informations, please try again."}
    
    else:
        return render_template('register.html')
#endregion


# Always leave those lines at the end of the file. 
# If not, will not take into account the code under it
if __name__ == "__main__":
    app.run(debug=True)