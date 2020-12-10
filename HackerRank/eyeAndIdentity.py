import numpy
numpy.set_printoptions(legacy='1.13')

def printIdentity(N, M):
    return numpy.eye(N, M)



if __name__ == '__main__':
    string = input()
    N = int(string[0])
    M = int(string[2])   
    print(printIdentity(N, M))
