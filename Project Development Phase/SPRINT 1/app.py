
from flask import Flask, render_template, request, redirect, session, url_for
import ibm_db
import re


app = Flask(__name__)


# for connection
# conn= ""

app.secret_key = 'a'



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    global userid
    msg = ''
    return render_template('signup.html',msg=msg)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/')
def base():
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():
    global userid
    msg = ''
    return render_template('login.html',msg=msg)
if __name__ == "__main__":
    app.run(debug=True)