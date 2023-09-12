def is_abundant(num):
    # Function to check if a number is abundant
    if num < 12:
        return False
    divisors_sum = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i
    return divisors_sum > num

def find_abundant_numbers(limit):
    # Generate a list of abundant numbers up to the given limit
    abundant_numbers = [num for num in range(12, limit + 1) if is_abundant(num)]
    return abundant_numbers

def main(limit):
    abundant_numbers = find_abundant_numbers(limit)
    can_be_written_as_sum = [False] * (limit + 1)

    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            if abundant_numbers[i] + abundant_numbers[j] <= limit:
                can_be_written_as_sum[abundant_numbers[i] + abundant_numbers[j]] = True
            else:
                break

    result = sum(i for i in range(1, limit + 1) if not can_be_written_as_sum[i])
    return result

if __name__ == "__main__":
    limit = 28123
    result = main(limit)
    print(f"The sum of positive integers that cannot be written as the sum of two abundant numbers up to {limit} is {result}")
