# Write a Python program to read first n lines of a file.

 
fl=open('text4.txt','a')
fl=open('text4.txt','r')

n=int(input('How Many Lines Are You Read:'))

for i in range(n):
    print(fl.readline())
    
    
       