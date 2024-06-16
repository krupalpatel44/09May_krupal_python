# Write a Python program to unzip a list of tuples into individual lists.

tuple_list=[(12,2,24,3),('This','Is','Python'),(8,4,5,76,87,32)]
count=1
for i in tuple_list:
    print(f'list {count}:{list(i)}')
    count+=1
    