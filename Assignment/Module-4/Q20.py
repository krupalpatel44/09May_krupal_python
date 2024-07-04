# Write python program that user to enter only odd numbers, else will raise an exception.

try:
    n=int(input('Enter Your Number: '))

    if n%2==0:
        raise EnvironmentError(n)
    print('You Enterd odd Number:',n)
except ValueError:
    print('Error!...Please Enter Valid Number...')