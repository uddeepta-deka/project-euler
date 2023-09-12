import numpy as np

def get_largest_prime_factor(N):
    """ This function returns the largest prime factor of N. """
    if N%2==0:
        lastFactor=2
        N = int(N/2)
        while N%2==0:
            N=int(N/2)
    else:
        lastFactor=1
    factor=3
    maxFactor = int(np.sqrt(N))
    while N>1 and factor<=maxFactor:
        if N%factor==0:
            N=int(N/factor)
            lastFactor=factor
            while N%factor==0:
                N=int(N/factor)
            maxFactor=np.sqrt(N)
        factor+=2
    if N==1:
        return lastFactor
    else:
        return N
    
if __name__ =="__main__":
    N = 600851475143
    print(f"The largest prime factor of {N} is: {get_largest_prime_factor(N)}")