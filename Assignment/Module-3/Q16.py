# Write a Python program to check whether a list contains a sub list.

list=[1,2,3,['Hello','25'],8,10.5]



for i in list:
    if type(i) == 'list':
        print("Yes")