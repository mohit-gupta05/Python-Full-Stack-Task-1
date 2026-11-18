from src.exceptions.student_exceptions import (
    StudentNotFoundError,
    DuplicateStudentError
)


class StudentService:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for existing in self.students:
            if existing.student_id == student.student_id:
                raise DuplicateStudentError("Student ID already exists.")

        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display_info()
            print("----------------")

    def update_student(self, student_id, new_name, new_age, new_course):
        for student in self.students:
            if student.student_id == student_id:
                student.name = new_name
                student.age = new_age
                student.course = new_course
                print("Student updated successfully!")
                return

        raise StudentNotFoundError("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        raise StudentNotFoundError("Student not found.")

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Student Found:")
                student.display_info()
                return

        raise StudentNotFoundError("Student not found.")