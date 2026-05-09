# Smart Task Management System

A robust, full-stack Task Management web application built with Python, Flask, PostgreSQL, and WebSockets. It features dynamic user authentication, real-time updates without page reloads, and intelligent analytics using Pandas and NumPy.

## Features

1. **Authentication**: Secure User Registration, Login, and Logout using `Flask-Login` and `Flask-Bcrypt`.
2. **REST API**: Complete CRUD APIs for tasks (`Add`, `Update`, `Delete`, `Get All`).
3. **PostgreSQL Integration**: Uses `Flask-SQLAlchemy` to store User and Task data persistently.
4. **Analytics Module**: Utilizes `Pandas` and `NumPy` to process and deliver precise insights (Total Tasks, Completed Tasks, Pending Tasks, and Completion Percentage).
5. **WebSocket Real-Time Updates**: Leverages `Flask-SocketIO` to push live task updates to the frontend instantly without refreshing.
6. **Responsive UI**: A modern, colorful frontend crafted with HTML and vanilla CSS to provide an exceptional user experience.

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL Server installed and running

### 1. Database Setup

Create a PostgreSQL database named `task_manager`. You can do this via `pgAdmin` or the `psql` command line:

```sql
CREATE DATABASE task_manager;
```

### 2. Installation

Clone this repository and open a terminal in the project directory.

Create a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

Install dependencies:
```powershell
pip install -r requirements.txt
```

### 3. Configuration & Execution

A `run.ps1` PowerShell script is provided to easily start the application. 
Open `run.ps1` and update the database credentials if necessary:

```powershell
$env:DB_USER = "postgres"
$env:DB_PASSWORD = "your_postgresql_password_here" # Update this!
$env:DB_HOST = "localhost"
$env:DB_NAME = "task_manager"
```

Run the application:
```powershell
.\run.ps1
```

The application will be accessible at `http://localhost:5000`.

### 4. Demo Video
*https://youtu.be/sDoD0_wqajY*

## Technologies Used
- **Backend**: Python, Flask
- **Database**: PostgreSQL, SQLAlchemy
- **Data Analytics**: Pandas, NumPy
- **Real-Time**: WebSockets (Flask-SocketIO)
- **Frontend**: HTML5, CSS3, JavaScript (Fetch API)
