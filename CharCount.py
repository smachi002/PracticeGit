str1 = 'adjdbas'
d = {}
for i in str1:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
print(d)