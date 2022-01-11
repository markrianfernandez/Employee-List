from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/employee'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
def Index():
    all_data = Data.query.all()

    return render_template("index.html", employees= all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':

        first_name = request.form['first_name']
        second_name = request.form['second_name']
        hiring_date = request.form['hiring_date']
        specialization = request.form['specialization']

        my_data = Data(first_name, second_name, hiring_date, specialization)
        db.session.add(my_data)
        db.session.commit()

        flash("New employee inserted successfully!")

        return redirect(url_for('Index'))

@app.route('/update', methods= ['GET', 'POST'])
def update():
     if request.method == 'POST':
         my_data = Data.query.get(request.form.get('id'))

         my_data.first_name = request.form['first_name']
         my_data.second_name = request.form['second_name']
         my_data.hiring_date = request.form['hiring_date']
         my_data.specialization = request.form['specialization']

         db.session.commit()
         flash("Employee updated successfully!")

         return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee deleted successfully!")

    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)