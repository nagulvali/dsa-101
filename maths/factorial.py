

def factorial(n):
    sum = 1
    for i in range(2, n+1):
        sum = sum * i
    return sum


def factorial_recursive(n):

    if n == 0:
        return 1

    return n * factorial_recursive(n-1)





if __name__ == '__main__':
    print(factorial(4))
    print(factorial_recursive(4))