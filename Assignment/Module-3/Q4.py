# Write a Python function to get the largest number, smallest num and sum of all from a list.


list=[1,5,6,3,4,8,9,7,2]

largest_num=list[0]
smallest_num=list[0]
total_sum=0

for i in list:
    if i>largest_num:
        largest_num=i
    if i<smallest_num:
        smallest_num=i
    total_sum+=i
    
print("largest number of list:",largest_num)
print("smallest number of list:",smallest_num)
print("sum of list:",total_sum)


    
        
            
