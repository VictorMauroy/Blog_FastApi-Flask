from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index Page<h1>'

@app.route('/Welcome/')
def welcome():
    return render_template('welcome.html')

@app.route('/User/<name>')
def get_user(name):
    return render_template('one_user.html', user_name=name)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user_name']
        return redirect(url_for('success', name=user))
    else:
        # user = request.args.get('user_name')
        # return redirect(url_for('success', name=user))
        return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'



# Always leave those lines at the end of the file. 
# If not, will not take into account the code under it
if __name__ == "__main__":
    app.run(debug=True)