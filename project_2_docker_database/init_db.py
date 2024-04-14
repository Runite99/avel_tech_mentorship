# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the credentials from the secured .env file
import os
from dotenv import load_dotenv
load_dotenv('credentials.env')

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = 'localhost' # different than inside the container and assumes default port of 3306

# Connect to the database
db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
cursor = db.cursor()

# Create a Compliments table (wrapping it in a try-except is good practice)
try:
  cursor.execute("""
    CREATE TABLE CUSTOMER_LIST (
      id                 integer  AUTO_INCREMENT PRIMARY KEY,
      coordinates        VARCHAR(60) NULL DEFAULT NULL,
      invite             TINYINT(1)
    );
  """)
  print("Creating Compliments table...")
except:
  print("Compliments Table already exists. Not recreating it.")


print('---------- DATABASE INITIALIZED ----------')
[print(x) for x in cursor]

db.close()