#create a simple  student management system using python dictionaries. Each student have the following information:
#PRN, Name, Course and Phone number. Write a Python program that allows users to perform the following operations 


"""add new student
Display all student
Search student by Name
Delete a student"""

# Define functions to perform operations
def add_student(students):
    PRN = input("Enter the Student PRN: ")
    name = input("Enter the Student name: ")
    course = input("Enter the Student Course: ")
    phone = input("Enter the Student Phone number: ")
    students[PRN] = {"Name": name, "Course": course, "Phone": phone}
    print("Student added successfully!")

def display_students(students):
    if not students:
        print("No students in the database.")
    else:
        for PRN, student in students.items():
            print(f"PRN: {PRN}, Name: {student['Name']}, Course: {student['Course']}, Phone: {student['Phone']}")

def search_student(students, name):
    found = False
    for PRN, student in students.items():
        if student["Name"].lower() == name.lower():
            print(f"PRN: {PRN}, Name: {student['Name']}, Course: {student['Course']}, Phone: {student['Phone']}")
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student(students, PRN):
    if PRN in students:
        del students[PRN]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Initialize student database
students = {}

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by Name")
    print("4. Delete Student by PRN")
    print("5. Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        print("Diplaying th List of Student")
        display_students(students)
    elif choice == "3":
        name = input("Enter the Student name to search: ")
        search_student(students, name)
    elif choice == "4":
        print("Searched Sudent")
        PRN = input("Enter the Student PRN to delete: ")
        delete_student(students, PRN)
    elif choice == "5":
        print("Exited.")
        break
    else:
        print("Invalid choice. Please try again.")

   
