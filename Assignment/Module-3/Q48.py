# Write a Python function to calculate the factorial of a number (a nonnegative integer)


def fact(num):
    count=1
    if num<0:
        print('factorial number is not calculate for nagative number.')
    elif num==0:
        print('factorial number is calculate to zero.')
    elif num>=0:
        for i in range(1,num+1):
            count*=i
            print(f'the factorial of {num} is {count}')

find_fectorial=int(input('enter number to find factorial:'))
fact(find_fectorial)


