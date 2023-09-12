__author__ = "Uddeepta Deka"

def get_factors(N):
    """ This function finds and returns the number of factors of N """
    num_factors = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            num_factors += 2
    if int(N**0.5) * int(N**0.5) == N:
        num_factors -= 1
    return num_factors

if __name__=="__main__":
    MAX_FACTORS = 500
    num_factors=0
    i=1
    while num_factors<MAX_FACTORS:
        i+=1
        triangle_num = int(i*(i+1)/2)
        num_factors = get_factors(triangle_num)
    print(f"The first triangle number to have over {MAX_FACTORS} divisors is {triangle_num}")