from flask import flask
app = Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome to the Python Flask Application"
@app.route('/greet/<username>')
def greet(username):
    return f"Hello, {username}"
@app.route('/farewell/<username>')
def farewell(username):
    return f"GoodBye, {username}"
if __name__ == '__main__':
    app.run(debug=True)