import math
def count_digits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1

print(count_digits(10200325)) # Output: 8


def count_digits_recursive(n):
    if n < 10:
        return 1
    return 1 + count_digits_recursive(n // 10)

print(count_digits_recursive(10200325)) # Output: 8


def count_digits_loop(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count if count > 0 else 1

print(count_digits_loop(10200325)) # Output: 8

