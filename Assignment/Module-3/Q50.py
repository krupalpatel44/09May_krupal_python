# Write a Python function to check whether a number is perfect or not.


num=int(input('enter your number:'))

sum=0

for i in range(1,num):
    if num%i == 0:
        sum+=i

if sum==num:
    print(f'yess...{num} is a  perfect number.')
else:
    print(f'no...{num} is not a perfect number')
    
