
from src.models.student import Student
from src.services.student_service import StudentService
from src.services.student_storage import StudentStorage
from src.exceptions.student_exceptions import (
    StudentNotFoundError,
    DuplicateStudentError
)

service = StudentService()
storage = StudentStorage()

# Load existing students
saved_data = storage.load_students()

for data in saved_data:
    student = Student(
        data["student_id"],
        data["name"],
        data["age"],
        data["course"]
    )
    service.students.append(student)


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")

            if not name.strip() or not course.strip() or age <= 0:
                print("Please enter valid details.")
            else:
                student = Student(student_id, name, age, course)

                try:
                    service.add_student(student)
                    storage.save_students(service.students)
                except DuplicateStudentError as e:
                    print(e)

        except ValueError:
            print("Please enter valid numeric values.")

    elif choice == "2":
        service.view_students()

    elif choice == "3":
        try:
            student_id = int(input("Enter Student ID to update: "))
            new_name = input("Enter New Name: ")
            new_age = int(input("Enter New Age: "))
            new_course = input("Enter New Course: ")

            if not new_name.strip() or not new_course.strip() or new_age <= 0:
                print("Please enter valid details.")
            else:
                try:
                    service.update_student(
                        student_id, new_name, new_age, new_course
                    )
                    storage.save_students(service.students)
                except StudentNotFoundError as e:
                    print(e)

        except ValueError:
            print("Please enter valid numeric values.")

    elif choice == "4":
        try:
            student_id = int(input("Enter Student ID to delete: "))

            try:
                service.delete_student(student_id)
                storage.save_students(service.students)
            except StudentNotFoundError as e:
                print(e)

        except ValueError:
            print("Please enter a valid Student ID.")

    elif choice == "5":
        try:
            student_id = int(input("Enter Student ID to search: "))

            try:
                service.search_student(student_id)
            except StudentNotFoundError as e:
                print(e)

        except ValueError:
            print("Please enter a valid Student ID.")

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please select 1 to 6.")
