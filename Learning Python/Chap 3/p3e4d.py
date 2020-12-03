L = [2 ** i for i in range(7)]
X = 5
pot = 2 ** X

if pot in L:
	print('at index', L.index(pot))
	
else:
	print(X, 'not found')