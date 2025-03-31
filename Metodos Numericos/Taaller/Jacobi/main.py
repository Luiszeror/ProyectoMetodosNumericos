from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=25,x=None):
    if x is None:
        x = zeros(len(A[0]))

    D = diag(A)
    R = A - diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - dot(R,x)) / D
    return x

A=np.array([4,0,-0.33,0], [-2,5,0,-0.33],[0,3.33,9,-1.5], [-0.66,0,2,6])
b=([0.5,0.25,0.16,0.33])
c= array([1.0,1.0])

result = jacobi(A,b,N=25,x=c)

            print "A:"
            pprint(A)

            print "b:"
            pprint(b)

            print "x:"
            print(result)