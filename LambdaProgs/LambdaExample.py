# Syntax: lambda value:Expr
# Example1:- Addition of 2 digits
addition = lambda a, b: a + b
print(addition(5, 6))

# Example2:- Square of 1 digit
square = lambda a: a * a
print(square(5))

# Example3:- Concate firstname and last name

full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
print(full_name('    swapnil', 'machikar'))

# Example4:- Sort list by last name
l = ['Swapnil Machikar', 'Sayali P Pandit', 'Arun B Wadekar']
l.sort(key=lambda name: name.split(' ')[-1].lower())
print(l)

# Example5:- Sort list of tuples by second value
l = [(2, 5), (1, 2), (4, 4)]
l.sort(key=lambda n: n[1])
print(l)

#Example6:- Intersection of 2 lists

l = [0,1,2,3]
l1 = [2,3,0]
l3 = list(filter(lambda x:x in l, l1))
print(l3)
