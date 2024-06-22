import logging
def validate_contact_number(contact_number):
    return contact_number.isdigit() and len(contact_number) == 10

def validate_name(name):
    return name.isalpha()

def add_student(students):
    while True:
        serial_number = input("Enter a Serial Number: ")
        if serial_number in students:
            print("Serial Number already exists. Please try again.")
            continue
        first_name = input("Enter a First Name: ")
        if not validate_name(first_name):
            print("Invalid name. Please enter alphabetic characters only.")
            continue
        last_name = input("Enter a Last Name: ")
        if not validate_name(last_name):
            print("Invalid name. Please enter alphabetic characters only.")
            continue
        contact_number = input("Enter a Contact Number: ")
        if not validate_contact_number(contact_number):
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
        logging.info(f"Added student: {students[serial_number]}")
        print("Student added successfully.")
        break

def remove_student(students):
    serial_number = input("Enter the Serial Number of the student to remove: ")
    if serial_number in students:
        confirm = input(f"Are you sure you want to remove student {serial_number}? (y/n): ")
        if confirm.lower() == 'y':
            del students[serial_number]
            logging.info(f"Removed student with Serial Number: {serial_number}")
            print("Student removed successfully.")
        else:
            print("Operation cancelled.")
    else:
        print("Student with Serial Number {} does not exist.".format(serial_number))

def view_all_students(students):
    if not students:
        print("No students found.")
        return
    for serial_number, info in students.items():
        print(f"\nSerial Number: {serial_number}")
        print(f"First Name: {info['fname']}")
        print(f"Last Name: {info['lname']}")
        print(f"Contact Number: {info['contact']}")
        print("Subjects:")
        for subject, details in info['subjects'].items():
            print(f"  {subject}: Marks = {details['marks']}, Fees = {details['fees']}")

def view_specific_student(students):
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
        print("Student with Serial Number {} does not exist.".format(serial_number))

def add_marks_to_student(students):
    serial_number = input("Enter the Serial Number of the student to add marks: ")
    if serial_number in students:
        subject = input("Enter the subject: ")
        if subject in students[serial_number]['subjects']:
            marks = input(f"Enter marks for {subject}: ")
            students[serial_number]['subjects'][subject]['marks'] = marks
            logging.info(f"Added marks for student {serial_number} in subject {subject}: {marks}")
            print(f"Marks added successfully for {subject}.")
        else:
            print(f"Subject {subject} not found for student {serial_number}.")
    else:
        print("Student with Serial Number {} does not exist.".format(serial_number))

def counsellor_menu(students):
    while True:
        print("\nCounsellor Menu:")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View specific student")
        choice = input("Enter a choice by counsellor: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            remove_student(students)
        elif choice == '3':
            view_all_students(students)
        elif choice == '4':
            view_specific_student(students)
        else:
            print("Invalid choice. Please try again.")
        
        more = input("Do you want to perform more operations? (y/n): ")
        if more.lower() != 'y':
            break

def faculty_menu(students):
    while True:
        print("\nFaculty Menu:")
        print("1. Add marks to student")
        print("2. View all students")
        choice = input("Enter a choice by Faculty: ")

        if choice == '1':
            add_marks_to_student(students)
        elif choice == '2':
            view_all_students(students)
        else:
            print("Invalid choice. Please try again.")

        more = input("Faculty wants to perform any other operations? (y/n): ")
        if more.lower() != 'y':
            break

def main():
    students = {}
    while True:
        print("\nRole Selection:")
        print("Press 1 for Counsellor")
        print("Press 2 for Faculty")
        print("Press 3 for Student")
        role = input("Enter a role id: ")

        if role == '1':
            counsellor_menu(students)
        elif role == '2':
            faculty_menu(students)
        elif role == '3':
            print("Student functionality is not implemented in this example.")
        else:
            print("Invalid role id. Please try again.")

if __name__=="__main__":
    main()
    
    


