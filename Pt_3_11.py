from pprint import pprint 
d = dict()
d = {a: a ** 3 for a in range(1,11) if a % 2 == 0 }
pprint(d)
