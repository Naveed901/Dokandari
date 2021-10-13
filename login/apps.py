from flask import Flask, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_json import FlaskJSON, JsonError, json_response, as_json
import re
import phonenumbers 
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





