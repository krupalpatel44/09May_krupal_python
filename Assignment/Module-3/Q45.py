# Write a Python program to find the highest 3 values in a dictionary.


dict={'cotlin':85, 'java':80, 'python':99, 'reactjs':50, 'c++':60}

list=[]

for i in dict.values():
    list.append(i)
    
list.sort()

print('dictionary:',dict)
print('highest 3 values:',list[-3:])

