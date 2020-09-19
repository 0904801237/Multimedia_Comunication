import math
import numpy
def nCk(N, k) : return numpy.prod( [(N-k+i)/i for i in range(1, k+1)] )
    # n! / (k! * (n-k)!) = ((n-k+1)*(n-k+2)*...*n )/ (1*2*3*...*k)
def prob(k, p, N) : 
    '''p(k)'''
    return nCk(N, k)*(p**k)*((1-p)**(N-k))

def sumProb(N, p) : 
    ''' sumProb function: total of probability of all symbols from 1 to N '''
    return sum( prob(k, p, N) for k in range(1,N+1) )

def infoMeasure(k, p, N) :
    ''' infoMeasure function: amount of information that symbol k carries '''
    return -math.log2( prob(k, p, N) )

def approxEntropy(N,p) : return sum( prob(k, p, N) * infoMeasure(k, p, N) for k in range(1,N+1) )

print(approxEntropy(5, 0.5))