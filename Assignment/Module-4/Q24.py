# Write a Python class named Circle constructed by a radius and two methods which will compute 
# the area and the perimeter of a circle


class circle:
    
    def con_area(self):
        pi=3.14
        ra=int(input('Enter value of radius:'))
        
        area=pi*(ra*ra)
        
        print("Area of circle is:",area)
        
    def perimeter(self):
        pi=3.14
        ra=int(input('Enter value of radius:'))
        
        pe=2*pi*ra
        print("perimeter of circle is:",pe)
        

c=circle()
c.con_area()
c.perimeter()


        