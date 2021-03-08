from flask import Flask, render_template, request, url_for

app = Flask(__name__)

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