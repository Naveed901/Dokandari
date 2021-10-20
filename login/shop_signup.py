from apps import *

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
  
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/',methods=["POST","GET"])
def index():
    return render_template('index.html')
 
@app.route("/upload",methods=["POST","GET"])
def upload():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':
        file = request.files.getlist('file[]')
        #print(files)
        #for file in files:
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cur.execute("INSERT INTO images (file_name, uploaded_on) VALUES (%s, %s)",[filename, now])
            mysql.connection.commit()
        print(file)
        cur.close()   
        flash('File(s) successfully uploaded')    
    return redirect('/')

# http://localhost:5000/pythinlogin/register - this will be the 
#    registration page, we need to use both GET and POST requests
@app.route('/dokandari/shop_signup/', methods=['POST'])
def shop_signup():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" "contact info" POST requests exist (user submitted form)
    if request.method == 'POST' and 'fullname' in request.form and 'password' in request.form and 'confirm_password' in request.form and 'email' in request.form and 'contact' in request.form and 'shopcontact' in request.form and 'city' in request.form and 'market' in request.form and 'shopname' in request.form and 'shopaddress' in request.form and 'squestion' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        password = request.form['password']
        cpassword = request.form['confirm_password']
        email = request.form['email']
        contact = request.form['contact']
        shopcontact = request.form['shop_contact']
        city = request.form['city']
        market = request.form['market']
        shopname = request.form['shopname']
        shopaddress = request.form['shopaddress']
        squestion = request.form['squestion']
            # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (fullname,))
        account = cursor.fetchone()
            # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', fullname):
            msg = 'Username must contain only characters and numbers!'
        elif not re.match(r'[z0-9]+', contact):
            my_contact = contact
            contact = phonenumbers.parse(my_contact, "PK")
            msg = 'Contact must contain only numbers!'
        elif not re.match(r'[z0-9]+', shopcontact):
            shop_contact = shopcontact
            my_number = phonenumbers.parse(shop_contact, "PK")
            msg = 'Contact must contain only numbers!'    
        elif not re.match(r'[A-Za]+', city):
            msg = 'City must contain only characters!'
        elif not re.match(r'[A-Za]+', market):
            msg = 'Market must contain only characters!'
        elif not re.match(r'[A-Za]+', shopname):
            msg = 'Shopname must contain only characters!'
        elif not re.match(r'[A-Za-z0-9]+', shopaddress):
            msg = 'Shopaddress must contain only characters and numbers!'
        elif not re.match(password == cpassword):
            msg = 'Password not match!'    
        elif not fullname or not password or not cpassword or not email or not contact or not city or not market or not shopname or not shopaddress or not squestion:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (fullname, password, cpassword, email, contact, city, market, shopname, shopaddress, squestion,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
        # Show registration form with message (if any)
    return json_response('shop_signup.html', msg=msg)



 