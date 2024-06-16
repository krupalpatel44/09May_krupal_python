# How can you pick a random item from a range?

import random

def random_num(num1,num2):
    random_num=random.choice(range(num1,num2))
    print('Random Number From Range Between is:',random_num)
    
First_num=int(input('Enter First Number:'))
Last_num=int(input('Enter Last Number:'))

random_num(First_num,Last_num)

