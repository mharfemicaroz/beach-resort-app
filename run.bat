@echo off
echo Starting frontend server...
cd C:\beach resort app\frontend
start cmd /k npm run dev --host

echo Starting MySQL server...
cd C:\xampp\mysql\bin\
start cmd /k mysqld.exe

echo Starting backend server...
cd C:\beach resort app\backend
start cmd /k python manage.py runserver 8080

echo Opening Chrome with http://localhost:5173/...
start chrome http://localhost:5173/