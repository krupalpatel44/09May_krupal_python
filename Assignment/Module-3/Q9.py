 # Write a Python function that takes two lists and returns true if they have at least one common member.
 
list1=['krupal','viraj','devin','karan']
list2=['kelvin','laxit','harshil','viraj']

common_member=[]
 
for i in list1:
    for j in list2:
        if i is j:
            common_member.append(i)


if len(common_member)>0:
    print("True...")
else:
    print("False...") 
 