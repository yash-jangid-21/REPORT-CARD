# Student Project Report Card

Welcome to the Student Project Report Card application! This Django-based web application allows educators to create, manage, and view report cards for students, streamlining the assessment process.

## Features

- **User Authentication**: Secure login and registration for educators.
- **Create Report Cards**: Easily generate report cards for individual students.
- **View and Edit Report Cards**: View existing report cards and make edits as necessary.
- **Responsive Design**: A user-friendly interface that works on both desktop and mobile devices.

## Technologies Used

- **Django**: The main web framework used for building the application.
- **SQLite**: The default database for storing report card data.
- **HTML/CSS**: For front-end design and layout.
- **Bootstrap**: For responsive design.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yash-jangid-21/Report-Card.git
    cd REPORT-CARD
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/

## Configuration

The application uses default Django settings. For production use, consider configuring additional settings such as `ALLOWED_HOSTS`, `DEBUG`, and database settings in `settings.py`.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please contact [yash062105@gmail.com](mailto:yash062105@gmail.com).

---

Thank you for checking out this project.
