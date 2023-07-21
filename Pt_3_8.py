from pprint import pprint
d = dict()
b = []
for i in range(97, 123):
    b.append(chr(i))
for i in range(0, 26):
    d[b[i]] = i
pprint(d)
