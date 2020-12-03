def min1(*args):
    res = args[0]
    for arg in args[1:]:
    if arg < res:
    res = arg
    return res

def min2(first, *rest):
    for arg in rest:
    if arg < first:
    first = arg
    return first

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

def max1(*args):
    res = args[0]
    for arg in args[1:]:
    if arg > res:
    res = arg
    return res

def max2(first, *rest):
    for arg in rest:
    if arg > first:
    first = arg
    return first

def max3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[-1]
