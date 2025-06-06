from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime
from flasgger import Swagger

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

swagger = Swagger(app)

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    hiring_date = db.Column(db.Date, default=date.today())
    specialization = db.Column(db.String(200))

    def __init__(self, first_name, second_name, hiring_date, specialization):
        self.first_name = first_name
        self.second_name = second_name
        self.hiring_date = hiring_date
        self.specialization = specialization


@app.route('/')
@app.route('/home')
def index():
    """
    Employee List
    ---
    get:
      description: Get all employees
      responses:
        200:
          description: A list of employees
    """
    all_data = Data.query.all()
    return render_template("index.html", employees=all_data)

@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Add Employee
    ---
    post:
      description: Add a new employee
      parameters:
        - name: first_name
          in: formData
          type: string
          required: true
        - name: second_name
          in: formData
          type: string
          required: true
        - name: hiring_date
          in: formData
          type: string
          format: date
          required: true
        - name: specialization
          in: formData
          type: string
          required: true
      responses:
        302:
          description: Redirect to employee list
    get:
      description: Render add employee form
      responses:
        200:
          description: Add employee form
    """
    if request.method == 'POST':
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        hiring_date_str = request.form['hiring_date']
        specialization = request.form['specialization']

        try:
            hiring_date = datetime.strptime(hiring_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash("Invalid date format. Please use YYYY-MM-DD.")
            return "Invalid date format", 400

        my_data = Data(first_name, second_name, hiring_date, specialization)
        db.session.add(my_data)
        db.session.commit()

        flash("New employee added successfully!")
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """
    Edit Employee
    ---
    post:
      description: Edit an existing employee
      parameters:
        - name: id
          in: path
          type: integer
          required: true
        - name: first_name
          in: formData
          type: string
          required: true
        - name: second_name
          in: formData
          type: string
          required: true
        - name: hiring_date
          in: formData
          type: string
          format: date
          required: true
        - name: specialization
          in: formData
          type: string
          required: true
      responses:
        302:
          description: Redirect to employee list
    get:
      description: Render edit employee form
      parameters:
        - name: id
          in: path
          type: integer
          required: true
      responses:
        200:
          description: Edit employee form
    """
    my_data = Data.query.get_or_404(id)
    if request.method == 'POST':
        my_data.first_name = request.form['first_name']
        my_data.second_name = request.form['second_name']
        hiring_date_str = request.form['hiring_date']
        try:
            my_data.hiring_date = datetime.strptime(hiring_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash("Invalid date format. Please use YYYY-MM-DD.")
            return "Invalid date format", 400
        my_data.specialization = request.form['specialization']

        db.session.commit()
        flash("Employee updated successfully!")
        return redirect(url_for('index'))

    return render_template('edit.html', emp=my_data)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    """
    Delete Employee
    ---
    post:
      description: Delete an employee
      parameters:
        - name: id
          in: path
          type: integer
          required: true
      responses:
        302:
          description: Redirect to employee list
    """
    my_data = Data.query.get_or_404(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee deleted successfully!")
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
