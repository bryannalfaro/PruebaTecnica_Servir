from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 
from decouple import config
  
app = Flask(__name__) 
  
# Connect to the database 
conn = psycopg2.connect(
    dbname=config('DB_CONNECTION'), 
    user=config('USER'), 
    password=config('PASSWORD_DB'), 
    host=config('HOST'), 
    port=config('PORT'),
) 

cur = conn.cursor() 
  
cur.execute( 
    '''SELECT * FROM department''') 
  
# close the cursor and connection 
cur.close() 
conn.close() 