__author__ = "Uddeepta Deka"

import inflect

def num_to_lett(n):
    p = inflect.engine()
    return p.number_to_words(n, andword="and", zero="zero")

def main():
    count = 0
    for num in range(1, 1001):
        num_in_words = num_to_lett(num)
        for char in num_in_words:
            if char.isalpha():
                count+=1
    print(count)
    return

if __name__ =="__main__":
    main()