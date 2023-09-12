__author__ = "Uddeepta Deka"
def factorial(n):
    """ Returns factorial of n. """
    if n==1:
        return 1
    else:
        return n*(factorial(n-1))
    
def main():
    N = 100
    factorial_N = str(factorial(N))
    print(f"The sum of digits in the number {N}! is:", sum(int(val) for val in factorial_N))

if __name__ == "__main__":
    main()