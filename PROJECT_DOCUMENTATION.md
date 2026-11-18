# Project Documentation
## Student Management System

### 1. Project Overview
The Student Management System is a console-based application developed using Python. It helps users manage student records through a simple menu-driven interface.

### 2. Project Objectives
- Learn Python programming fundamentals.
- Implement Object-Oriented Programming (OOP).
- Work with lists and objects.
- Handle errors and exceptions.
- Store and retrieve student records using JSON.

### 3. Technologies Used
- Python
- JSON
- Visual Studio Code
- Git and GitHub

### 4. Project Features
1. Add Student – Add a new student record.
2. View Students – Display all student records.
3. Update Student – Modify existing student details.
4. Delete Student – Remove a student record.
5. Search Student – Find a student using Student ID.
6. Exit – Close the application.

### 5. Project Structure
- `main.py` – Main application and menu.
- `src/models/student.py` – Student class.
- `src/services/student_service.py` – Student management operations.
- `src/services/student_storage.py` – JSON file handling.
- `src/exceptions/student_exceptions.py` – Custom exceptions.
- `student_data.json` – Stores student records.
- `README.md` – Project introduction and instructions.
- `screenshots/` – Project screenshots.

### 6. OOP Concepts
The project uses a Student class to represent student records and a StudentService class to manage student operations.

### 7. Exception Handling
The application handles invalid numeric input, duplicate Student IDs, and student records that cannot be found. File operations also handle common errors.

### 8. File Handling
Student records are stored in JSON format. The application loads saved records when it starts and saves changes after successful add, update, and delete operations.

### 9. How to Run
1. Open the Task-1 folder in VS Code.
2. Open the terminal.
3. Run the command:

```bash
python main.py
```

### 10. Testing
The following operations were tested:
- Adding a student.
- Viewing student records.
- Updating student details.
- Deleting a student.
- Searching for a student.
- Handling duplicate Student IDs.
- Handling invalid input and missing records.
- Saving and loading student data.

### 11. Conclusion
This project demonstrates practical use of Python fundamentals, OOP, data structures, exception handling, JSON file handling, and GitHub version control.

**Internship Task:** Task 1 – Student Management System