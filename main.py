students = []

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    students.append({"name": name, "age": age, "course": course})
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No records found.\n")
    else:
        for s in students:
            print(s)
        print()

def search_student():
    name = input("Enter name to search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print(s)
            return
    print("Student not found.\n")

def delete_student():
    name = input("Enter name to delete: ")
    global students
    students = [s for s in students if s["name"].lower() != name.lower()]
    print("Student deleted if existed.\n")

while True:
    print("1. Add 2. View 3. Search 4. Delete 5. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice\n")
