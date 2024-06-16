# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.


def find_min_max(num):
    max_num=max(num)
    min_num=min(num)
    
    print('maximum number:',max_num)
    print('minimum number:',min_num)
    
decimal_number=[12.5,3.14,2.5,4.78,34.95,12.5,7.6,8.3]
    
find_min_max(decimal_number)