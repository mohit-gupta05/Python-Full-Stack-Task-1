
import json
import os


class StudentStorage:

    FILE_PATH = "student_data.json"

    def save_students(self, students):
        data = []

        for student in students:
            data.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course
            })

        try:
            with open(self.FILE_PATH, "w") as file:
                json.dump(data, file, indent=4)

            print("Student data saved successfully!")

        except OSError as e:
            print("Error saving student data:", e)

    def load_students(self):
        if not os.path.exists(self.FILE_PATH):
            return []

        try:
            with open(self.FILE_PATH, "r") as file:
                data = json.load(file)

            return data

        except json.JSONDecodeError:
            print("Error: Student data file contains invalid JSON.")
            return []

        except OSError as e:
            print("Error loading student data:", e)
            return []
