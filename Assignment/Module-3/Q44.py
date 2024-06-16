# Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary. 
#Sample data: {'1': ['a','b'], '2': ['c','d']} 
#Expected Output: 
#ac ad bc bd


dict1={'1':['a','b'],'2':['c','d']}

print('dict:',dict1)
print('expected output:')

dict2=[]
for i in dict1.values():
    dict2.append(i)
    
length=len(dict2)

for j in range(length):
    for k in range(length):
        x=dict2[0][j]+dict2[1][k]
        print(x,end='')
    