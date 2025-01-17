import math

def vector_add(v, w):
    """Adds corresponding elements."""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]
    
def vector_subtract(v, w):
    """Subtracts corresponding elements."""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]
    
def vectors_sum(vectors):
    """Sums all corresponding elements."""
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector."""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """Compute vector whose ith element is the mean of the ith elements of the input vectors."""
    n = len(vectors)
    return scalar_multiply(1/n, vectors_sum(vectors))

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))
    
def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v_1 - w_1 + ... + v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

