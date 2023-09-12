__author__ = "Uddeepta Deka"

import numpy as np

def get_factors(N):
    """ This function finds and returns the factors of N """
    factors = [1]
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            factors.append(i)
            factors.append(int(N/i))
    return list(set(factors))

def find_amicable(Nmax):
    checks = [True]*Nmax
    pairs_list = []
    for i in range(2, Nmax):
        if checks[i]:
            sum_fac = int(sum(get_factors(i)))
            if sum_fac!=i:
                sum_alternate = sum(get_factors(sum_fac))
                if sum_alternate == i:
                    checks[i]=False
                    checks[sum_fac]=False
                    pairs_list.append((i, sum_fac))
    return pairs_list

def main():
    Nmax = 10000
    amicable_list = np.array(find_amicable(Nmax)).flatten()
    print(f"The sum of all amicable numbers under {Nmax} is {sum(amicable_list)}.")
    
if __name__=="__main__":
    main()
