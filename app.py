from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/select-entity')
def select_entity():
    return render_template('select-entity.html')

#employees
@app.route('/all-employees')
def all_employees():
    return render_template('all-employees.html')
@app.route('/new-employee')
def new_employee():
    return render_template('new-employee.html')
@app.route('/del-employee')
def del_employee():
    return render_template('del-employee.html')
@app.route('/edit-employee')
def edit_employee():
    return render_template('edit-employee.html')

#departments
@app.route('/all-departments')
def all_departments():
    return render_template('all-departments.html')
@app.route('/new-department')
def new_department():
    return render_template('new-department.html')
@app.route('/del-department')
def del_department():
    return render_template('del-department.html')
@app.route('/edit-department')
def edit_department():
    return render_template('edit-department.html')

if __name__ == '__main__':
    app.run(debug=True)