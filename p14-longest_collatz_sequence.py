__author__ = "Uddeepta Deka"

import time

def collatz_sequence(num, memo):
    """ 
    This function returns the length of a collatz sequence
    whose starting point is num. It uses cache to reduce calculations.
    """
    len_count = 0
    n = num
    while num>1:
        if num%2==0:
            num = int(num/2)
        else:
            num = int(3*num+1)
        len_count+=1
        if num in memo:
            memo[n] = memo[num] + len_count
            break
    return memo[n]

if __name__ == "__main__":
    start_time = time.perf_counter()
    MAX_START_NUM = 1000000
    max_length = 0
    start_num = 0
    memo = {}
    memo[1] = 1
    for i in range(2, MAX_START_NUM):
        length = collatz_sequence(i, memo)
        if length > max_length:
            max_length = length
            start_num = i
    end_time = time.perf_counter()
    print(f"Starting number under {MAX_START_NUM} with longest Collatz sequence is {start_num} with length {max_length}.")
    print(f"Computation time taken = {end_time-start_time:0.3f}s.")