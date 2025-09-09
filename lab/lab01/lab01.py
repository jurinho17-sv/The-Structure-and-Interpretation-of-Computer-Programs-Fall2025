# Lab 1: Functions

"""
Q3: Pick a Digit
Implement digit, which takes positive integers n and k and has only a single return statement as its body. It returns the digit of n that is k positions to the left of the rightmost digit (the one's digit). If k is 0, return the rightmost digit. If there is no digit of n that is k positions to the left of the rightmost digit, return 0.

Hint: Use // and % and the built-in pow function to isolate a particular digit of n.
"""

def digit(n, k):
    """Return the k-th digit from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """

    # divide by 10^k
    # then take % 10 to isolate the last digit
    return (n // pow(10, k)) % 10

# ------------------------------------------

"""
Q4: Middle Number
Implement middle by writing a single return expression that evaluates to the value that is neither the largest or smallest among three different integers a, b, and c.

Hint: Try combining all the numbers and then taking away the ones you don't want to return by using the built-in min and max functions.

"""
def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    # add up all three
    # subtract the smallest
    # then subtract the largest
    return a + b + c - min(a, b, c) - max(a, b, c)

# ------------------------------------------

"""
Q7: Falling Factorial
Let's write a function falling, which is a "falling" factorial that takes two arguments, n and k, and returns the product of k consecutive numbers, starting from n and working downwards. When k is 0, the function should return 1.
"""
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """

    total = 1

    while k > 0:
        total = total * n
        n -= 1
        k -= 1

    return total

# ------------------------------------------

'''
Q8: Divisible By k
Write a function divisible_by_k that takes positive integers n and k. It prints all positive integers less than or equal to n that are divisible by k from smallest to largest. Then, it returns how many numbers were printed.
'''
def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 that are divisible by 7
    >>> c
    0
    """
    i = 1
    count = 0

    while i <= n:
        if i % k ==0:
            print(i)
            count += 1
        i += 1
    return count

# ------------------------------------------

'''
Q9: Sum Digits
Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)
'''
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    sum = 0
    while y > 0:        # must be y > 0 to avoid an infinite loop when y = 0
        sum += y % 10
        y = y // 10
    return sum

# ------------------------------------------

'''
Q10: Double Eights
Write a function that takes in a number and determines if the digits contain two adjacent 8s.
'''
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    prev_digit = 0

    while n > 0:
        current_digit = n % 10
        if current_digit == 8 and prev_digit == 8:
            return True
        prev_digit = current_digit
        n = n // 10
    return False