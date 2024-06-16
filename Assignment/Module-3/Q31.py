# How will you create a dictionary using tuples in python?


tuple_1=(1,2,3,4,5)
tuple_2=('krupal','devin','karan','viraj','kelvin')

total=len(tuple_1)

dict_list={}

for i in range(total):
    dict_list[tuple_1[i]]=tuple_2[i]
    
    print(dict_list)