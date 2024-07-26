# :page_facing_up: Text to HTML Converter

A Django-based web application that converts plain text into HTML. This project demonstrates how to build a simple text-to-HTML converter using the Django framework and SQLite as the backend.

## Features

- :memo: **Text Input**: Enter plain text to be converted into HTML.
- :mag: **Preview**: View the converted HTML output in real-time.
- :floppy_disk: **Save**: Save the converted HTML content.

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Django**: Web framework used for building the application.




## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.0 or higher

### Installation Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/anurag-srivatsav/Text2Html.git
    cd text-to-html-django
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

## Usage

### Running the Application

To start the application, run the following command:
```bash
python manage.py runserver
```

### Accessing the Application

Once the server is running, you can access the application at `http://localhost:8000`. Use the interface to enter plain text and convert it to HTML. You can also log in to the Django admin panel at `http://localhost:8000/admin` using the superuser credentials you created.

## Demo

Check out the live demo: [Text to HTML Converter Demo](https://your-live-demo-url.com)





## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: [Anurag srivastav](anuragsrivatsav4@gmail.com)
- **GitHub**: [anurag-srivatsav](https://github.com/anurag-srivatsav)

---


