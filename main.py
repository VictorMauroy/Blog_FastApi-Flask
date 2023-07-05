from flask import Flask, render_template, request, url_for, redirect
from model import User, Post, Comment
from sqlalchemy.orm import Session
from connection import engine

app = Flask(__name__)

session = Session(bind=engine)

@app.route('/')
def feed():
    posts = session.query(Post).all()
    return render_template('index.html', posts=posts)

# @app.route('/User/<name>')
# def get_user(name):
#     return render_template('one_user.html', user_name=name)

#region Show and create Post

@app.route('/post/', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        message = request.form['message']

        # Should update later with an user session and a token
        current_user = session.query(User).get(1)

        new_post = Post(
            title= title,
            content=message,
            user=current_user
        )

        # INSERT INTO DATABASE the new post
        try:
            session.add(new_post)
            session.commit()
            return redirect('/') # Do not forget to update
        except:
            return {"error": "There is an issue to send your post, please try again."}

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
            # Should later return to main/index page with an effective connection
            return redirect(url_for('success', name=username))
        else:
            # Should replace it later by an error.html page with a parameter "error name".
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

        # Refuse to register the guest if duplicate username or email.
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