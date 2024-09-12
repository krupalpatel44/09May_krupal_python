student = {}

while True:
    print("               \nRole Selection:")
    print("                Press 1 for Counsellor")
    print("                Press 2 for Faculty")
    print("                Press 3 for Student")
    role=input("Enter Your Roll Id: ")
    
    if role =='1':
        while True:
            print("             \nCounsellor Menu:")
            print("              1. Add student")
            print("              2. Remove student")
            print("              3. View all students")
            print("              4. View specific student")
            choice=input("Enter a choice by counceller: ")
            
            if choice=='1':
                while True:
                    serial_number= input("Enter Your Serial Number:")
                    if serial_number in student:
                        print("Serial Number already exists. Please try again.")
                        continue
                
        
    
    
