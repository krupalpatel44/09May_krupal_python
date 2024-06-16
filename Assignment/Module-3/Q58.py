# Write a Python program to read a random line from a file.


import random

file=open("list.txt",'r')

read_line=file.readlines()
random_line=random.choice(read_line)
print(random_line)


