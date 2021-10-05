from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app)

# http://localhost:5000/pythinlogin/register - this will be the 
#    registration page, we need to use both GET and POST requests
@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" "contact info" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'contact' in request.form and 'city' in request.form and 'market' in request.form and 'shopname' in request.form and 'shopaddress' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        contact = request.form['contact']
        city = request.form['city']
        market = request.form['market']
        shopname = request.form['shopname']
        shopaddress = request.form['shopaddress']
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

email = request.form['email']

 # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not re.match(r'[z0-9]+', contact):
            msg = 'Contact must contain only numbers!'    
        elif not re.match(r'[A-Za]+', city):
            msg = 'City must contain only characters!'
        elif not re.match(r'[A-Za]+', market):
            msg = 'Market must contain only characters!'
        elif not re.match(r'[A-Za]+', shopname):
            msg = 'Shopname must contain only characters!'
        elif not re.match(r'[A-Za-z0-9]+', shopaddress):
            msg = 'Shopaddress must contain only characters and numbers!'    
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s)', (username, password, email, contact, city, market, shopname, shopaddress,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'