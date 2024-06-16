# How can you pick a random item from a list or tuple?


import random
list=[12,'python','java',24,40,'android',55]
tuple=(1,2,3,4,5,6,7,8,9,0)

random_list=random.choice(list)
random_tuple=random.choice(tuple)

print('List:',list)
print("The Random Number From List Is:",random_list)

print('Tuple:',tuple)
print("The Random Number From Tuple Is:",random_tuple)



