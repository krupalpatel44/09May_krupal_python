# Write a Python program to remove an empty tuple(s) from a list of tuples.


tuple_list=[(10,12,6,8),('This','Is','a','Python'),(20,18,13,5,6,7,),()]


for i in tuple_list:
    if len(i)==0:
        tuple_list.remove(i)
        
print("Remov in Empty tuple from tuple_list:",tuple_list)