# Write a Python program to convert degree to radian


def convert(degree):
    radian=degree * (3.14/180)
    print('coversation after degree to radian:',radian)
    
degree=int(input('enter degree:'))

convert(degree)

