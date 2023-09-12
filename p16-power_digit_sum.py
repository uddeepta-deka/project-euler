import time
start = time.perf_counter()
num = str(2 ** 1000)
end = time.perf_counter()
print(sum(int(digit) for digit in num))
print(f"Computation time: {end-start:0.3f}s")