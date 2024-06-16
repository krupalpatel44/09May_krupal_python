# Write a Python function to check whether a number is in a given range.


def check_number(check_num, start_num, end_num):
    if check_num in range(start_num,end_num):
        print(f'the {check_num} number is between {start_num} to {end_num}')
    else:
        print(f'the {check_num} number is not between {start_num} to {end_num}')

start_num=int(input('enter start number:'))
end_num=int(input('enter end number:'))
check_num=int(input('enter number to check:'))

check_number(check_num, start_num, end_num)
        
