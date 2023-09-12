__author__ = "Uddeepta Deka"

import time
def find_primes(N):
    """ 
    This function returns all primes upto N.
    It uses The sieve of Eratosthenes algorithm.
    """
    primes = [2]
    sieve = [True] * N
    for i in range(3, N, 2):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, N, i):
                sieve[j] = False
    return primes

if __name__ == "__main__":
    start = time.perf_counter()
    MAX_PRIME = 2000000
    primes = find_primes(MAX_PRIME)
    print(f"The sum of all primes up to {MAX_PRIME} is {sum(primes)}.")
    end = time.perf_counter()
    print(f"Compute time={end-start:0.3f}s.")
