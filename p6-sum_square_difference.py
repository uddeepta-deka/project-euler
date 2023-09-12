min = 1
max = 10
sum_of_squares = sum(x*x for x in range(min, max+1))
squares_of_sum = sum(x for x in range(min, max+1))**2

print(f"The difference = {squares_of_sum-sum_of_squares}")