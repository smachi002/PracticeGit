l = ['a','b','c']
l1 = ['d','c','b']

new_list = list(map(lambda n1,n2:n1+n2, l,l1))
print(new_list)

for i in new_list:
    print(i)