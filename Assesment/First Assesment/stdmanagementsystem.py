students = {}

while True:
    print("               \nRole Selection:")
    print("                Press 1 for Counsellor")
    print("                Press 2 for Faculty")
    print("                Press 3 for Student")
    role = input("Enter a role id: ")

    if role == '1':  # Counsellor Menu
        while True:
            print("             \nCounsellor Menu:")
            print("              1. Add student")
            print("              2. Remove student")
            print("              3. View all students")
            print("              4. View specific student")
            choice = input("Enter a choice by counsellor: ")

            if choice == '1':  # Add student
                while True:
                    serial_number = input("Enter a Serial Number: ")
                    if serial_number in students:
                        print("Serial Number already exists. Please try again.")  
                        continue
                    first_name = input("Enter a First Name: ")
                    if not first_name.isalpha():
                        print("Invalid name. Please enter alphabetic characters only.")
                        continue
                    last_name = input("Enter a Last Name: ")
                    if not last_name.isalpha():
                        print("Invalid name. Please enter alphabetic characters only.")
                        continue
                    contact_number = input("Enter a Contact Number: ")
                    if not (contact_number.isdigit() and len(contact_number) == 10):
                        print("Invalid contact number. Please enter a 10-digit number.")
                        continue

                    subjects = {}
                    while True:
                        subject = input("Enter a Subject (or type 'done' to finish): ")
                        if subject.lower() == 'done':
                            break
                        marks = input("Enter marks for {}: ".format(subject))
                        fees = input("Enter fees for {}: ".format(subject))
                        subjects[subject] = {'marks': marks, 'fees': fees}
                    
                    students[serial_number] = {
                        'fname': first_name,
                        'lname': last_name,
                        'contact': contact_number,
                        'subjects': subjects
                    }
                    print("Student added successfully.")
                    break

            elif choice == '2':  # Remove student
                serial_number = input("Enter the Serial Number of the student to remove: ")
                if serial_number in students:
                    confirm = input(f"Are you sure you want to remove student {serial_number}? (y/n): ")
                    if confirm.lower() == 'y':
                        del students[serial_number]
                        print("Student removed successfully.")
                    else:
                        print("Operation cancelled.")
                else:
                    print(f"Student with Serial Number {serial_number} does not exist.")

            elif choice == '3':  # View all students
                if not students:
                    print("No students found.")
                else:
                    for serial_number, info in students.items():
                        print(f"\nSerial Number: {serial_number}")
                        print(f"First Name: {info['fname']}")
                        print(f"Last Name: {info['lname']}")
                        print(f"Contact Number: {info['contact']}")
                        print("Subjects:")
                        for subject, details in info['subjects'].items():
                            print(f"  {subject}: Marks = {details['marks']}, Fees = {details['fees']}")

            elif choice == '4':  # View specific student
                serial_number = input("Enter the Serial Number of the student to view: ")
                if serial_number in students:
                    info = students[serial_number]
                    print(f"\nSerial Number: {serial_number}")
                    print(f"First Name: {info['fname']}")
                    print(f"Last Name: {info['lname']}")
                    print(f"Contact Number: {info['contact']}")
                    print("Subjects:")
                    for subject, details in info['subjects'].items():
                        print(f"  {subject}: Marks = {details['marks']}, Fees = {details['fees']}")
                else:
                    print(f"Student with Serial Number {serial_number} does not exist.")

            else:
                print("Invalid choice. Please try again.")
            
            more = input("Do you want to perform more operations? (y/n): ")
            if more.lower() != 'y':
                break

    elif role == '2':  # Faculty Menu
        while True:
            print("         \nFaculty Menu:")
            print("         1. Add marks to student")
            print("         2. View all students")
            choice = input("Enter a choice by Faculty: ")

            if choice == '1':  # Add marks to student
                serial_number = input("Enter the Serial Number of the student to add marks: ")
                if serial_number in students:
                    subject = input("Enter the subject: ")
                    if subject in students[serial_number]['subjects']:
                        marks = input(f"Enter marks for {subject}: ")
                        students[serial_number]['subjects'][subject]['marks'] = marks
                        print(f"Marks added successfully for {subject}.")
                    else:
                        print(f"Subject {subject} not found for student {serial_number}.")
                else:
                    print(f"Student with Serial Number {serial_number} does not exist.")

            elif choice == '2':  # View all students
                if not students:
                    print("No students found.")
                else:
                    for serial_number, info in students.items():
                        print(f"\nSerial Number: {serial_number}")
                        print(f"First Name: {info['fname']}")
                        print(f"Last Name: {info['lname']}")
                        print(f"Contact Number: {info['contact']}")
                        print("Subjects:")
                        for subject, details in info['subjects'].items():
                            print(f"  {subject}: Marks = {details['marks']}, Fees = {details['fees']}")

            else:
                print("Invalid choice. Please try again.")

            more = input("Faculty wants to perform any other operations? (y/n): ")
            if more.lower() != 'y':
                break
            else:
                  print("Invalid role id. Please try again.")
