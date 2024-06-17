print("                                STUDENT MANAGEMENT SYSYTEM")

def info():
    print("For Counseller   Press-1")
    print("For Faculty  Press-2")
    print("For Student  Press-3")
    
info()
option=int(input("Enter Your Role Id:"))


if option==1:
    print("           1. Add Student")
    print("           2. Remove Student")
    print("           3. View All Students")
    print("           4. View Specific Student")
    coun=int(input("Enter a chioce by counseller:"))
    x=input("Enter Your Student Number:")
    
if option==2:
    print("          Add Mark to Students  press 1")
    print("          View All Students   press 2")
    faculty=input("Enter a choice by Faculty:")
    
    addmark=int(input("Enter Marks:"))
    print("Enter Marks:",addmark)
    

    sn=int(input("Enter a Serial Number:"))
    fn=input("Enter a First Name:")
    ln=input("Enter a Last Name:")
    cn=int(input("Enter a Contact Number:"))
    sub=input("Enter a Subject:")
    mark=int(input("Enter a Marks:"))
    fees=int(input("Enter a Fees:"))
    sub1=input("Enter a Subject:")
    mark1=int(input("Enter a Mark:"))
    fees1=int(input("Enter a Fees:"))
   
    
    
    if coun==1:
        print("Enter a Serial Number:",sn)
        print("Enter a First Name:",fn)
        print("Enter a Last Name:",ln)
        print("Enter a Contact Number:",cn)
        print("Enter a Subject:",sub)
        print("Enter a Marks:",mark)
        print("Enter a Fees:",fees)
        print("Enter a Subject:",sub1)
        print("Enter a Marks:",mark1)
        print("Enter a Fees:",fees1)
    

    

        
        
        
        
       
        
        
        
        

    