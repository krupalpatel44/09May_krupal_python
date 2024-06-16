# Write a Python program to check whether an element exists within a tuple.


t=[]

data=int(input("Enter Number Of Data:"))

for i in range(data):
    n=int(input("Enter Number:"))
    t.append(n)
t1=tuple(t)
print(t1)

check=int(input("Check A Number:"))

if check in t1:
    print("Your Number Is Exits...",)
else:
    print("Your Number Is Not Exits...")
    
    