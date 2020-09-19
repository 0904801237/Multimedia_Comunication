import math
import numpy
def nCk(N, k) : return numpy.prod( [(N-k+i)/i for i in range(1, k+1)] )
    # n! / (k! * (n-k)!) = ((n-k+1)*(n-k+2)*...*n )/ (1*2*3*...*k)
def prob(k, p, r) : 
    '''p(k)'''
    return nCk(k, k-r+1) * (p**r) * ((1-p)**(k-r))

def sumProb(N, p, r) : 
    ''' sumProb function: total of probability of all symbols from 1 to N '''
    return sum( prob(k, p, r) for k in range(1,N+1) )

def infoMeasure(k, p, r) :
    ''' infoMeasure function: amount of information that symbol k carries '''
    return -math.log2( prob(k, p, r) )

def approxEntropy(N, p, r) : return sum( prob(k, p, r) * infoMeasure(k, p, r) for k in range(1,N+1) )

print(approxEntropy(5, 0.5, 3))