__author__ = "Uddeepta"

def check_multiple(x):
    """ This function checks if a given number is a multiple of either 3 or 5 """
    is_multiple=False
    if (x%5==0) or (x%3==0):
        is_multiple=True
    return is_multiple

def main():
    print("This program finds the sum of all the multiples of 3 or 5 below 1000")
    sum = 0
    for x in range(0, 1000):
        if check_multiple(x):
            sum+=x
    print(f"The sum is = {sum}")
    return

if __name__ == "__main__":
    main()