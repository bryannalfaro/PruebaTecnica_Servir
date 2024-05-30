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
    #GET DEPARTMENT BY CODE
    def getDepartmentByCode(self, code_dept):
        self.cursor.execute('SELECT * FROM department WHERE code_dept = %s', (code_dept,))
        return self.cursor.fetchone()
    
    #GET EMPLOYEE BY CODE
    def getEmployeeByCode(self, code_employee):
        self.cursor.execute('SELECT * FROM employee WHERE code_employee = %s', (code_employee,))
        return self.cursor.fetchone()
    
    #GET EMPLOYEES OF DEPARTMENT
    def getNumEmployees(self, code_dept):
        self.cursor.execute('SELECT COUNT(dept_employee) from employee where dept_employee= %s', (code_dept,))
        return self.cursor.fetchone()  
    #ALL DEPARTMENTS AND EMPLOYEES
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
    
    #CREATE DEPARTMENTS AND EMPLOYEES
    def createDepartment(self, code_dept, name_dept, description_dept):
        code_exist  = self.getDepartmentByCode(code_dept)
        if code_exist != None:
            return 'EXISTE DEPARTAMENTO'
        else:
            print(code_dept, name_dept, description_dept)
            self.cursor.execute('''
                        INSERT INTO department (code_dept, name_dept, description_dept) VALUES 
                            (%s, %s, %s)''',(code_dept, name_dept, description_dept)) 
            self.db_connection.commit()
    
    def createEmployee(self, name_employee, last_employee, birth_employee, code_employee):
        code_exist = self.getDepartmentByCode(code_employee)
        if code_exist != None:
            self.cursor.execute('''
                        INSERT INTO employee (name_employee, last_name_employee, date_of_birth_employee, dept_employee)
                                VALUES (%s, %s, %s, %s)''',(name_employee, last_employee, birth_employee, code_employee))
            self.db_connection.commit()
        else:
            return 'NO EXISTE DEPARTAMENTO'
        
    #DELETE EMPLOYEE AND DEPARTMENT
    def deleteDepartment(self, code_department):
        code_exist = self.getDepartmentByCode(code_department)
        num_employees = self.getNumEmployees(code_department)

        if code_exist != None:
            if num_employees[0] == 0:
                self.cursor.execute('''
                            DELETE FROM department WHERE code_dept = %s''',(code_department,))
                self.db_connection.commit()
            else:
                return 'EL DEPARTAMENTO TIENE EMPLEADOS'
        else:
            return 'NO DEPARTMENT'
    
    def deleteEmployee(self, code_employee):
        code_exist = self.getEmployeeByCode(code_employee)
        if code_exist != None:
            self.cursor.execute('''
                        DELETE FROM employee WHERE code_employee = %s''',(code_employee,))
            self.db_connection.commit()
        else:
            return 'NO EMPLOYEE'
        
        