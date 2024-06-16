# Write a Python program to calculate the area of a parallelogram.


def parallelogram(base,height):
    parallelogram=base*height
    print('area of parallelogram:',parallelogram)
    
base=int(input('Enter value of base:'))
height=int(input('Enter value of height:'))

parallelogram(base,height)
