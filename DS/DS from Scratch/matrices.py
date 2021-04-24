import math

def shape(A):
    """Given a list-of-lists representation of a matrix, the matrix A has len(A) rows and len(A[0]) columns
    that is the shape of the matrix A."""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    """If a matrix has n rows and k columns we can refer to it as an n x k matrix, each of the n rows of the 
    matrix is a vector of length k."""
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j]
            for A_i in A]
    
def make_matrix(num_rols, num_cols, entry_fn):
    """returns a num_rols x num_cols matrix whose (i,j)th entry is fn(i, j)"""
    return[[entry_fn(i, j)
            for j in range(num_cols)]
           for i in range(num_rols)]
    
def is_diagonal(i, j):
    """1's on the diagonal', 0 everywhere else"""
    return 1 if i == j else 0




    