
def add(a, *args):
	print(type(args))
	ans = 0
	for n in args:
		ans += n
	print(ans)

add(4, 3, 4, 1, 2)

def culc(n, **kwargs):
	print(type(kwargs))
	print(kwargs)
	for key, value in kwargs.items():
		print(key)
		print(value)
	n += kwargs["add"]
	n *= kwargs["multiply"]
	print(n)

culc(2, add=3, multiply=5)


