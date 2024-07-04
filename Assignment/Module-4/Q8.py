# Write a python program to find the longest words.


fl=open('text8.txt')

data=fl.readlines()
a=max(data,key=len)
print(a)


    






