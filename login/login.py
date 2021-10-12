

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

   