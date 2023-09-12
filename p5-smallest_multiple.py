__author__ = "Uddeepta Deka"

# Function to calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the least common multiple (LCM) of two numbers
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Function to find the smallest positive number divisible by all numbers in the range [min, max]
def smallest_divisible(min, max):
    if min > max:
        min, max = max, min  # Swap min and max if necessary
    
    result = min
    for i in range(min + 1, max + 1):
        result = lcm(result, i)
    
    return result

if __name__=="__main__":
    # Input: Minimum and Maximum values
    min_value = 1
    max_value = 20
    smallest = smallest_divisible(min_value, max_value)
    print(f"The smallest positive number divisible by all numbers between {min_value} and {max_value} is:", smallest)