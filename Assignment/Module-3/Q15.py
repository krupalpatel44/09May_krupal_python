# Write a Python program to get unique values from a list.


a=[3,5,5,6,6,4,4,8,8,8,1,1]

b=[]

for i in a:
    if i not in b:
        b.append(i)
        
print(a)        
print("unique value in list:",b)




