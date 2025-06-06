import unittest
from app import app, db, Data
from datetime import date

class EmployeeListTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_index_empty(self):
        """Test index page with no employees"""
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertNotIn(b'No employees', rv.data)  # Assuming template shows something else if empty

    def test_add_employee_success(self):
        """Test adding a new employee successfully"""
        rv = self.app.post('/add', data={
            'first_name': 'John',
            'second_name': 'Doe',
            'hiring_date': '2023-01-01',
            'specialization': 'Engineering'
        }, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'New employee added successfully!', rv.data)
        with app.app_context():
            emp = Data.query.filter_by(first_name='John', second_name='Doe').first()
            self.assertIsNotNone(emp)
            self.assertEqual(emp.specialization, 'Engineering')

    def test_add_employee_invalid_date(self):
        """Test adding employee with invalid date format"""
        rv = self.app.post('/add', data={
            'first_name': 'Jane',
            'second_name': 'Doe',
            'hiring_date': 'invalid-date',
            'specialization': 'HR'
        })
        self.assertIn(rv.status_code, [400, 500])

    def test_edit_employee_success(self):
        """Test editing an existing employee successfully"""
        with app.app_context():
            emp = Data('Alice', 'Smith', date(2022, 5, 1), 'Marketing')
            db.session.add(emp)
            db.session.commit()
            emp_id = emp.id

        rv = self.app.post(f'/edit/{emp_id}', data={
            'first_name': 'Alice',
            'second_name': 'Johnson',
            'hiring_date': '2022-05-01',
            'specialization': 'Sales'
        }, follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Employee updated successfully!', rv.data)
        with app.app_context():
            emp = Data.query.get(emp_id)
            self.assertEqual(emp.second_name, 'Johnson')
            self.assertEqual(emp.specialization, 'Sales')

    def test_edit_employee_not_found(self):
        """Test editing a non-existent employee"""
        rv = self.app.post('/edit/9999', data={
            'first_name': 'Ghost',
            'second_name': 'User',
            'hiring_date': '2022-01-01',
            'specialization': 'None'
        })
        self.assertEqual(rv.status_code, 404)

    def test_delete_employee_success(self):
        """Test deleting an existing employee"""
        with app.app_context():
            emp = Data('Bob', 'Brown', date(2021, 7, 1), 'Finance')
            db.session.add(emp)
            db.session.commit()
            emp_id = emp.id

        rv = self.app.post(f'/delete/{emp_id}', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Employee deleted successfully!', rv.data)
        with app.app_context():
            emp = Data.query.get(emp_id)
            self.assertIsNone(emp)

    def test_delete_employee_not_found(self):
        """Test deleting a non-existent employee"""
        rv = self.app.post('/delete/9999')
        self.assertEqual(rv.status_code, 404)

    def test_index_with_employees(self):
        """Test index page with employees listed"""
        with app.app_context():
            emp1 = Data('Tom', 'Hanks', date(2020, 1, 1), 'Acting')
            emp2 = Data('Emma', 'Stone', date(2019, 2, 2), 'Acting')
            db.session.add_all([emp1, emp2])
            db.session.commit()

        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Tom', rv.data)
        self.assertIn(b'Emma', rv.data)

if __name__ == '__main__':
    unittest.main()
