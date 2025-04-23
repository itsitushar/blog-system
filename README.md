# Blog System Project

## Overview
This project is a Django-based blog system that allows users to list blogs, view blog details, and integrate external APIs (like the RestCountries API) to display additional information about countries.

## Features
- List all blogs
- View individual blog details
- Country information integration via RestCountries API
- Optional features: comments, likes, search/filter, user authentication

## Setup Instructions

### Prerequisites
- Python 3.x
- Django 5.2
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository-name
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Apply migrations:
   ```bash
   python manage.py migrate
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the blog system at `http://127.0.0.1:8000/` in your browser.

## License
Include any licensing information here, if applicable.
