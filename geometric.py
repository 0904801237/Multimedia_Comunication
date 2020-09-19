import math
def prob(n, p) :
    ''' prob function: Sucessful probability after n attempts 
                    n: The number of attempts
                    p: Sucessful probability of one attempts
    '''
    return p*((1-p)**(n-1))
def sumProb(N, p) :
    ''' sumProb function: total of probability of all symbols from 1 to N
            Examples: p = 0.5
            sumProb(10, 0.5) = 0.9990234375
            sumProb(25, 0.5) = 0.9999999701976776
            sumProb(50, 0.5) = 0.9999999999999991
            ...
            So if N -> ∞ then sumProb(N, 0.5) -> 1
    '''
    return sum(prob(syb, p) for syb in range(1,N+1))
def infoMeasure(n, p) :
    ''' infoMeasure function: amount of information that symbol x carries '''
    return -math.log2(prob(n, p))
def approxEntropy(N,p) :
    ''' approxEntropy function: avarage information sources of all symbols from 1 to N
            Examples: p = 0.5
            approxEntropy(10,0.5) = 1.98828125
            approxEntropy(25,0.5) = 1.9999991953372955
            approxEntropy(50,0.5) = 1.9999999999999538
            ...
            So if N -> ∞ then approxEntropy(N, 0.5) -> 2 ~ Entropy of geometric info. source with p = 0.5
    '''
    return sum(prob(isr, p) * infoMeasure(isr, p) for isr in range(1,N+1))