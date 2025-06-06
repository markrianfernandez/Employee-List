# Employee List Management Application

This is a Flask-based web application for managing an employee list. It provides CRUD (Create, Read, Update, Delete) operations for employee records, including first name, second name, hiring date, and specialization. The application uses SQLite as the database and includes API documentation with Swagger.

## Features

- List all employees
- Add a new employee
- Edit existing employee details
- Delete employees
- Input validation for hiring date
- Flash messages for user feedback
- API documentation using Flasgger (Swagger UI)
- Unit tests for core functionality

## Installation and Setup

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed.
3. Install required packages:
   ```
   pip install flask flask_sqlalchemy flasgger
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Access the application in your browser at `http://127.0.0.1:5000/`.

## Usage

- Navigate to the home page to see the list of employees.
- Use the "Add" page to add a new employee.
- Edit or delete employees using the respective buttons on the employee list.

## API Endpoints

- `GET /` or `/home`: List all employees.
- `GET /add`: Render form to add a new employee.
- `POST /add`: Add a new employee.
- `GET /edit/<id>`: Render form to edit an employee.
- `POST /edit/<id>`: Update employee details.
- `POST /delete/<id>`: Delete an employee.

## Testing

Unit tests are provided in `test_app.py` using Python's `unittest` framework. The tests cover:

- Loading the index page with and without employees
- Adding employees with valid and invalid data
- Editing existing employees and handling non-existent employees
- Deleting employees and handling non-existent employees

To run the tests:

```
python -m unittest test_app.py
```

## Technologies Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flasgger (Swagger UI)
- SQLite
- unittest (for testing)

## License

This project is open source and available under the MIT License.
