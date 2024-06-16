# Write a Python program to check multiple keys exists in a dictionary.


dict={'id':1, 'name':'krupal', 'sub':'python'}
dict_key=[]
new_key=['id','name','sub','city']

for i in dict:
    dict_key.append(i)
print('dict_key:',dict_key)
print('new_key:',new_key)

print('do all keys exists??')

if new_key==dict_key:
    print("true...")
else:
    print("false...")
    
    
        