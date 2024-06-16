"""Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30."""


first_5=[]
last_5=[]

for i in range(1,31):
    if i<=5:
        sqare=i*i
        first_5.append(sqare)
        
    if i> 25:
        sqare=i*i
        last_5.append(sqare)
        
print("Sqare Of First 5 Element:",first_5)
print("Sqare Of Last Member:",last_5)










