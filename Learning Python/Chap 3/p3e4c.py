L = [1, 2, 4, 8, 16, 32, 64]
X = 5
pot = 2 ** X

if pot in L:
	print('at index', L.index(pot))
	
else:
	print(X, 'not found')