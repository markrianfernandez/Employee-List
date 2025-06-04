# Employee Management Flask Application

## Description
This is a simple Flask web application for managing employees. It allows users to view a list of employees, add new employees, edit existing employee details, and delete employees. The application features a video background and styled UI components.

## Prerequisites
- Python 3.11 or higher
- Flask
- Other dependencies as listed in `requirements.txt` (if available)

## Installation
1. Clone the repository or download the project files.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is not available, install Flask manually:
   ```bash
   pip install Flask
   ```

## Running the Application
1. Ensure you are in the project root directory.
2. Run the Flask application:
   ```bash
   flask run
   ```
3. Open your web browser and navigate to `http://localhost:5000` to access the app.

## Features
- Employee list with details: first name, last name, gender, salary.
- Add new employee with form validation.
- Edit existing employee details.
- Delete employees.
- Video background and styled UI.
- Logo and background images for enhanced appearance.

## File Structure
- `app.py`: Main Flask application file.
- `templates/`: HTML templates for the web pages.
- `static/`: Static files including images and video backgrounds.
- `instance/`: Database files (SQLite).

## Usage
- Navigate to the home page to see the list of employees.
- Use the "+ Add New Employee" link to add a new employee.
- Use the "Edit" link next to each employee to modify their details.
- Use the "Delete" button to remove an employee.

## License
This project is provided as-is without any warranty.

---

Feel free to customize this README as needed for your project.
