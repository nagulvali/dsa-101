
def is_palindrome_number(n):
    original_number = n
    rev_number = 0

    while original_number != 0:
        temp = original_number % 10
        rev_number = rev_number*10 + temp

        original_number = original_number//10

    return rev_number == n


if __name__ == '__main__':
    print(is_palindrome_number(1201))
