# Hospital Management System (HMS)
A Hospital Management System built using Django and SQLite. This project helps manage hospital operations, including patient management, appointment scheduling, and more.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Patient registration and management
- Appointment scheduling
- Staff management
- Medical records management
- Simple and user-friendly interface

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- [Python](https://www.python.org/downloads/) (3.6 or later)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

## Installation
Follow these steps to set up the Hospital Management System on your local machine:

# Step 1: Clone the Repository
```bash
git clone https://github.com/Aduda-Shem/HMS.git
```
```bash
 cd HMS 
```
# Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```
# Step 3: Activate the Virtual Environment
```bash
  source venv/bin/activate
```

# Step 4: Install Required Packages
```bash
pip install -r requirements.txt
```
# Step 5: Run Database Migrations
```bash
python manage.py migrate
```
# Step 6: Create a Superuser
```bash
python manage.py createsuperuser
```
# Step 7: Run the Development Server
```bash
python manage.py runserver
```

After setup, you can access the Hospital Management System through your web browser:
1. Open your browser and go to `http://127.0.0.1:8000/`
2. Log in using the superuser credentials you created during installation
3. Start managing your hospital operations!
