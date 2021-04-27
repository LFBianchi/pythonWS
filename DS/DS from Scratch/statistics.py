import vectors
import matrices
import math
from collections import Counter

def mean(x):
    """The mean on the values on a vector x."""
    return sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    
    if n % 2 == 1:
        return sorted_v[midpoint]
    
    else:
        lo = midpoint - 1
        hi = midpoint + 1
        return (sorted_v[lo] + sorted_v[hi]) / 2
    
def quantile(x, p):
    """Returns the pth-percentile value in x."""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """returns a list,  might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in count.iteritems()
            if count == max_count]
    
def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """subtract the mean from every member of x."""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """X must have at least two elements."""
    if len(x) > 1:
        n = len(x)
        deviations = de_mean(x)
        return vectors.sum_of_squares(deviations) / (n - 1)
    else :
        return 0
    
def standard_deviation(x):
    return math.sqrt(variance(x))

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

