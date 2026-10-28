lst = [2, 3, 2, 5, 3, 2, 5, 8]
d = {}
for i in lst:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)