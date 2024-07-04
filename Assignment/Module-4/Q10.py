# Write a Python program to count the frequency of words in a file.


fl=open('text10.txt','a')
fl=open('text10.txt','r')


data=fl.read()

n=input("Enter Your Cherecter:")
count=0

for i in data:
    if i==n:
        count+=len(i)
        
print(count)
