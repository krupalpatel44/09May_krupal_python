# Write a Python program to read last n lines of a file.

fl=open('text5.txt','a')
fl=open('text5.txt','r')

n=int(input("How many last lines are you read:"))

read_Data=fl.readlines()[-n:]

for i in read_Data:
    print(i)