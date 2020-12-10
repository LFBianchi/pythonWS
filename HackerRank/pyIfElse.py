n = int(input().strip())
if not n % 2:
    if n in range(2, 6): print('Not Weird')
    elif n > 20: print('Not Weird')
    else: print('Weird')
else: print('Weird') 
