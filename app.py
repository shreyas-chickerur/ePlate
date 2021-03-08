from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/eplate_db.db'
db = SQLAlchemy(app)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('registration.html')

if (__name__ == "__main__"):
    app.run(debug=True)