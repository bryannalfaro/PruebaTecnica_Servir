from flask import Flask, render_template, request, flash, redirect
from model_system import ModelDB
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c53d6d9705933030f9ee8068f4872d60dff6820d0f80f19f'


model_db = ModelDB()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/select-entity')
def select_entity():
    return render_template('select-entity.html')

#employees
@app.route('/all-employees')
def all_employees():
    employees = model_db.getAllEmployees()
    return render_template('all-employees.html', employees=employees)

@app.route('/new-employee', methods=['POST', 'GET'])
def new_employee():
    departments = model_db.getAllDepartments()
    if request.method == "POST":
        name_employee = request.form.get('name-employee')
        last_name = request.form.get('last-employee')
        born_date = request.form.get('born-employee')
        code_dept = request.form.get('department-code')

        if name_employee == '' or last_name == '' or code_dept == '':
            flash('Please enter required data', 'Null data')
        else:
            insert_employee = model_db.createEmployee(name_employee, last_name, born_date, code_dept)
            if insert_employee != None:
                flash('Employee created successfully', 'Success')
            else:
                flash('Employee not created successfully', 'Error')
    return render_template('new-employee.html', departments=departments)

@app.route('/del-employee')
def del_employee():
    return render_template('del-employee.html')
@app.route('/edit-employee')
def edit_employee():
    return render_template('edit-employee.html')

#departments
@app.route('/all-departments')
def all_departments():
    departments = model_db.getAllDepartments()
    return render_template('all-departments.html', departments=departments)

@app.route('/new-department', methods=["GET","POST"])
def new_department():
    if request.method == "POST":
        code_dept = request.form.get('code-dept')
        name_dept = request.form.get('name-dept')
        description_dept = request.form.get('description-dept')

        if name_dept == '' or code_dept == '':
            flash('Please enter a name and a description', 'Null data')
        else:
            insert_dept = model_db.createDepartment(code_dept, name_dept, description_dept)
            if insert_dept=='None':
                flash('Exito', 'Success')
            else:
                flash('Codigo existente', 'Error')


        

    return render_template('new-department.html')
@app.route('/del-department')
def del_department():
    return render_template('del-department.html')
@app.route('/edit-department')
def edit_department():
    return render_template('edit-department.html')



if __name__ == '__main__':
    app.run(debug=True)