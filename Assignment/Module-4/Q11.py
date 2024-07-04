#   Write a Python program to write a list to a file.


list=['rajkot','surat','jamnagar','baroda',12,25]

fl=open('text11.txt','w')

for i in list:
    fl.write(f'{i}\n')
    
    
    
