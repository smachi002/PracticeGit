#Syntax:- map(function, Data(Iterable))
l = [1,2,3,4]
#without list it returns map object thats whay converted to list
new_list = list(map(lambda n:n**2, l))

print(new_list)