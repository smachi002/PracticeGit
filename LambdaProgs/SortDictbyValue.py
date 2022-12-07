city = ['Pune','Mum','Hyd']
temp = [8,7,9]
d = {}
for i in range(0,len(city)):
    d[city[i]] = temp[i]

details = sorted(d.items(), key=lambda n:n[1])
print(dict(details))
