from flask import Flask, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_json import FlaskJSON, JsonError, json_response, as_json
import re
app = Flask(__name__)
FlaskJSON(app)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dokandari'

# Intialize MySQL
mysql = MySQL(app)




# why login route support 2 methods? It should be POST only
@app.route('/login/', methods=['POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        # check user name and password for special characters. Search how to sanitize the input/mysql query. Username minumum should be checked
        # 
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            # {success:true,message:Logged in successfully!,data:account}
            return json_response ('Logged in successfully!')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return json_response('login.html', msg=msg)

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/dokandari/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 

   

# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/signup', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
        mysql.connection.commit()
        msg = 'You have successfully registered!'        
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return json_response('signup.html', msg=msg)


#     # Check if account exists using MySQL
# cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
# account = cursor.fetchone()
#                     # If account exists show error and validation checks
# if account:
#         msg = 'Account already exists!'
# elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#         msg = 'Invalid email address!'
# elif not re.match(r'[A-Za-z0-9]+', username):
#         msg = 'Username must contain only characters and numbers!'
# elif not username or not password or not email:
#         msg = 'Please fill out the form!'
# else:
#         # Account doesnt exists and the form data is valid, now insert new account into accounts table
#         cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
#         mysql.connection.commit()
#         msg = 'You have successfully registered!'                