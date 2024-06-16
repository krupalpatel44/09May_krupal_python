# Write a Python program to remove duplicates from a list.

a=[1,2,2,3,3,3,4,4,4,4]

b=[]

for i in a:
    if i not in b:
        b.append(i)
        
print("list after removing duplicates:",b)