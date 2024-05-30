from flask import Flask, render_template, request, flash, redirect, url_for
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
        
        return redirect(url_for('select_entity'))
    return render_template('new-employee.html', departments=departments)

@app.route('/del-employee', methods=['POST', 'GET'])
def del_employee():
    employees = model_db.getAllEmployees()

    if request.method == 'POST':
        print(request)
        code_employee = request.form.get('code-employee')
        print(code_employee)
        if code_employee != '':
            delete_employee = model_db.deleteEmployee(code_employee)
            if delete_employee != None:
                flash('No existe ', 'Error')
            else:
                flash('Employee deleted successfully', 'Success')
        else:
            flash('Employee not deleted successfully', 'Null data')
        
        return redirect(url_for('select_entity'))

    return render_template('del-employee.html', employees=employees)
@app.route('/edit-employee', methods=['POST', 'GET'])
def edit_employee():
    departments = model_db.getAllDepartments()
    if request.method == 'POST':
        code_employee = request.form.get('code-employee')
        name_employee = request.form.get('name-employee')
        last_employee = request.form.get('last-employee')
        born_employee = request.form.get('born-employee')
        code_dept = request.form.get('code-dept')
        #No update department code
        if code_dept == '':
            update_employee_without_code  = model_db.updateEmployeeWithoutDept(code_employee, name_employee, last_employee, born_employee)
            if update_employee_without_code != 'None':
                flash('No employee with code ', 'Error')
            else:
                flash('Success updating', 'Success')
        #Update with department code
        else:
            update_employee_with_code = model_db.updateEmployeeWithDept(code_employee, name_employee, last_employee, born_employee, code_dept)
            if update_employee_with_code != 'None':
                flash('Missing one code', 'Error')
            else:
                flash('Success updating', 'Success')
        return redirect(url_for('select_entity'))
    return render_template('edit-employee.html', departments=departments)

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
        return redirect(url_for('select_entity'))


        

    return render_template('new-department.html')
@app.route('/del-department', methods=['POST', 'GET'])
def del_department():
    departments = model_db.getAllDepartments()
    if request.method == 'POST':
        code_dept = request.form.get('department-code')
        if code_dept=='':
            flash('Debes ingresar un departamento', 'Null data')
        else:
            delete_dept = model_db.deleteDepartment(code_dept)
            if delete_dept == 'None':
                flash('Exito', 'Success')
            else:
                flash('Error en eliminacion', 'Error')
        return redirect(url_for('select_entity'))
    return render_template('del-department.html', departments = departments)

@app.route('/edit-department', methods = ['POST', 'GET'])
def edit_department():
    departments = model_db.getAllDepartments()
    if request.method == 'POST':
        code_dept = request.form.get('code-dept')
        name_dept = request.form.get('name-dept')
        description_dept = request.form.get('description-dept')

        if name_dept == '':
            name_dept = 'No name provided'
        elif description_dept == '':
            description_dept = 'No description provided'
        
        update_department = model_db.updateDepartment(code_dept, name_dept, description_dept)
        if update_department != 'None':

                flash('CODIGO NO EXISTE', 'Error')
        else:   
            flash('ACTUALIZACION EXITOSA', 'Success')
        return redirect(url_for('select_entity'))


    return render_template('edit-department.html', departments = departments)



if __name__ == '__main__':
    app.run(debug=True)