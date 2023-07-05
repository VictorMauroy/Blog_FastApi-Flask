from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/User/<name>')
# def get_user(name):
#     return render_template('one_user.html', user_name=name)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user_name']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}'



# Always leave those lines at the end of the file. 
# If not, will not take into account the code under it
if __name__ == "__main__":
    app.run(debug=True)