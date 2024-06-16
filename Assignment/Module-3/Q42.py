# Write a Python program to print all unique values in a dictionary.


dict={'a':100, 'b':200, 'c':300, 'd':200}

dict1=[]

for i,j in dict.items():
    if j not in dict1:
        dict1.append(j)
    
print('dict:',dict)
print('unique value in dictionary:',dict1)

