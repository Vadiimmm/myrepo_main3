a = int(input('введите a'))
b = int(input('введите b'))
c = int(input('введите c'))
if a >= b and a>=c:
	print(f'{a} наибольшее')
	max = a
	if b >= c:
	       print(f'{c} наименьшее')
	       print(f'{max} {b} {c}')
	else:
	        print(f'{b} наименьшее')
	        print(f'{max}{c}{ b}')
elif b >= a and b >=c:
	print(f'{b} наибольшее')
	max =b
	if a >= c:
	    	print(f'{c} наименьшее')
	    	print(f'{max}{a}{c}')
	else:
			print(f'{b} наименьшее')
			print(f'{max}{c}{a}')
else:
	print(f'{c} наибольшее')
	if b >= a:
	    	print(f'{a} наименьшее')
	    	print(f'{c}{ b} {a}')
	else:
			print(f'{b} наименьшее')
			print(f'{c} {a} {b}')
