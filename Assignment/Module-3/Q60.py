# Write a Python program to calculate the area of a trapezoid.

def trapezoid(top,bottom,height):
    trapezoid=((top+bottom)/2)*height
print('Area of trapezoid:',trapezoid)

top=int(input('Enter value of top:'))
bottom=int(input('Enter value of bottom:'))
height=int(input('Enter value of height:'))

trapezoid(top,bottom,height)


