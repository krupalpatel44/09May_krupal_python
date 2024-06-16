# Write a Python program to returns sum of all divisors of a number.


num=int(input('enter number:'))

sum=0

for i in range(1,num):
    if num%i == 0:
        sum+=i
        print('sum of all diviaora of a number is:',sum)
        
        