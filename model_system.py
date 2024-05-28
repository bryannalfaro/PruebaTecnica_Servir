from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 
import os
from dotenv import load_dotenv

load_dotenv()
  
app = Flask(__name__) 

# Connect to the database 
conn = psycopg2.connect(
    dbname=os.getenv('DB_CONNECTION'),
    user=os.getenv('USER'), 
    password=os.getenv('PASSWORD_DB'), 
    host=os.getenv('HOST'), 
    port=os.getenv('PORT'),
) 

cur = conn.cursor() 

cur.execute( 
    '''SELECT * FROM department''') 
  
# close the cursor and connection 
cur.close() 
conn.close() 