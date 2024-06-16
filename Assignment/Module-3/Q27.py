# Write a Python program to find the repeated items of a tuple.
t=(10,20,30,40,50,20,10)

list=[]

for i in t:
    if t.count(i) >= 2:
        list.append(i)


print("Repeated Touple Is:",tuple(set(list)))
