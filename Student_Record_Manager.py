# ==========================================
# PART I - STUDENT RECORD MANAGER
# Dynamic Array ADT
# ==========================================

# Student class
class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level


# Dynamic Array class
class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.students = [None] * self.capacity

    # Add Student
    def add(self, student):
        if self.size == self.capacity:
            self.resize()

        self.students[self.size] = student
        self.size += 1

    # Resize the array
    def resize(self):
        new_capacity = self.capacity * 2
        new_students = [None] * new_capacity

        for i in range(self.size):
            new_students[i] = self.students[i]

        self.students = new_students
        self.capacity = new_capacity

    # Display all students
    def display(self):
        if self.size == 0:
            print("\nNo students found.")
            return

        print("\n========== STUDENT RECORDS ==========")

        for i in range(self.size):
            student = self.students[i]

            print("Student ID:", student.student_id)
            print("Student Name:", student.student_name)
            print("Course:", student.course)
            print("Year Level:", student.year_level)
            print("-------------------------------------")

    # Search Student
    def search(self, student_id):
        for i in range(self.size):
            if self.students[i].student_id == student_id:
                return self.students[i]

        return None

    # Update Student
    def update(self, student_id, student_name, course, year_level):
        student = self.search(student_id)

        if student is not None:
            student.student_name = student_name
            student.course = course
            student.year_level = year_level
            return True

        return False

    # Remove Student
    def remove(self, student_id):
        index = -1

        # Find the student
        for i in range(self.size):
            if self.students[i].student_id == student_id:
                index = i
                break

        # Student not found
        if index == -1:
            return False

        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.students[i] = self.students[i + 1]

        self.students[self.size - 1] = None
        self.size -= 1

        return True

    # Display Array Information
    def display_info(self):
        print("\n========== ARRAY INFORMATION ==========")
        print("Number of Students:", self.size)
        print("Array Capacity:", self.capacity)


# ==========================================
# MAIN PROGRAM - PART I
# ==========================================

def student_record_manager():
    students = DynamicArray()

    while True:
        print("\n================================")
        print("     STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # Add
        if choice == "1":
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            year_level = int(input("Enter Year Level: "))

            student = Student(
                student_id,
                student_name,
                course,
                year_level
            )

            students.add(student)

            print("Student added successfully.")

        # Display
        elif choice == "2":
            students.display()

        # Search
        elif choice == "3":
            student_id = input("Enter Student ID to search: ")

            student = students.search(student_id)

            if student is not None:
                print("\nStudent Found!")
                print("Student ID:", student.student_id)
                print("Student Name:", student.student_name)
                print("Course:", student.course)
                print("Year Level:", student.year_level)
            else:
                print("Student not found.")

        # Update
        elif choice == "4":
            student_id = input("Enter Student ID to update: ")

            student = students.search(student_id)

            if student is not None:
                student_name = input("Enter New Student Name: ")
                course = input("Enter New Course: ")
                year_level = int(input("Enter New Year Level: "))

                students.update(
                    student_id,
                    student_name,
                    course,
                    year_level
                )

                print("Student updated successfully.")
            else:
                print("Student not found.")

        # Remove
        elif choice == "5":
            student_id = input("Enter Student ID to remove: ")

            if students.remove(student_id):
                print("Student removed successfully.")
            else:
                print("Student not found.")

        # Array Information
        elif choice == "6":
            students.display_info()

        # Exit
        elif choice == "7":
            print("Exiting Student Record Manager...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run Part I
student_record_manager()