from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 
from decouple import config
  
app = Flask(__name__) 

class ModelDB(object):
    def __init__(self):
        self.db_connection = psycopg2.connect(
                        dbname=config('DB_CONNECTION'), 
                        user=config('USER'), 
                        password=config('PASSWORD_DB'), 
                        host=config('HOST'), 
                        port=config('PORT'),
                        ) 
        
        self.cursor = self.db_connection.cursor()

    def getAllDepartments(self):
        self.cursor.execute('''
                            SELECT * FROM department
                            
                            ''')
        return self.cursor.fetchall()
        
    def getAllEmployees(self):
        self.cursor.execute('''
                            SELECT * FROM employee
                            ''')
        
        return self.cursor.fetchall()