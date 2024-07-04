# Write a Python program to copy the contents of a file to another file.


fl=open('text12.txt','a')
file=open('text6.txt','r')

for i in file:
    fl.write(i)
    
    