"""Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings."""


list = ['abc','aba','bca','bdb','cba','cac']
count=[]
for i in list:
    if len(i)>=2 and i[0]==i[-1]:
        count.append(i)
        
        
print(count)
