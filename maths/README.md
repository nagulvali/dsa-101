# Maths for DSA

## Sum Of N Natural Numbers
- sum of n natural numbers can be calculated using the formula: `n * (n + 1) // 2`
- below is the derivation of the formula:
```shell
1 + 2 + 3 + ... + n = S(n)
n + (n-1) + (n-2) + ... + 1 = S(n)
(n+1) + (n+1) + (n+1) + ... + (n+1) = 2 * S(n)
2 * S(n) = n * (n + 1)
S(n) = n * (n + 1) // 2
```

- Here is the Python implementation of the formula to calculate the sum of the first `n` natural numbers:
```python
def sum_of_n_natural_numbers(n):
    return n * (n + 1) // 2
```


## Count Digits in a Number
- To count the number of digits in a number, we can use the formula: `floor(log10(n)) + 1`
- Below is the derivation of the formula:
```shell
n = 10^0 + 10^1 + 10^2 + ... +
10^(d-1) where d is the number of digits in n
log10(n) = log10(10^0 + 10^1 + 10
^2 + ... + 10^(d-1))
log10(n) = 0 + 1 + 2 + ... + (d-1)
log10(n) = d - 1
d = log10(n) + 1
```
- Here is the Python implementation of the formula to count the number of digits in a number:
```python
import math
def count_digits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1
```
- [program](./count_digits.py)


## Palindrome Number
- A number is a palindrome if it reads the same backward as forward.
- To check if a number is a palindrome, we can reverse the number and compare it with the original number.
- Here is the Python implementation to check if a number is a palindrome:
```python
def is_palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num
```

## Factorial Number
- A factorial is the product of all positive integers from 1 to n.
- Example: factorial of 4 = 4*3*2*1
- Can be written as 4 * factorial(3) = n*(n-1)!
- Program: [factorial](./factorial.py)
- 
