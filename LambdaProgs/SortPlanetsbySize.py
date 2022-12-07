planets = [('Earth', 500), ('Mercury', 200)]

sorting = lambda n:n[1]
planets.sort(key= sorting)
print(planets)


l = [('Earth', 500), ('Mercury', 200)]

l.sort(key=lambda n:n[1])