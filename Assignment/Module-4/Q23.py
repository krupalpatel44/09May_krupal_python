# Write a Python class named Rectangle constructed by a length and width and a method which will 
# computer the area of a rectangle.


class rectangle:

    def area(self):
        length=int(input('Enter Value of length: '))
        width=int(input('Enter Value of Width: '))

        a=length * width

        print('Area Of Rectangle is:',a)

r=rectangle()

r.area()