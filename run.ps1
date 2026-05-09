$env:DB_USER = "postgres"
$env:DB_PASSWORD = "rika"
$env:DB_HOST = "localhost"
$env:DB_NAME = "task_manager"

Write-Host "Starting Smart Task Manager..."
Write-Host "Please make sure you have updated the PostgreSQL password in this script if it is not 'your_postgresql_password_here'"
Write-Host "And ensure the database 'task_manager' exists!"

.\venv\Scripts\python.exe app.py
