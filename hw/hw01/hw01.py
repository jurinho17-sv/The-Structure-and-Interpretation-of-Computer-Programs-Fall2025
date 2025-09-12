# Homework 1: Functions, Control

from operator import add, sub

# Q1: A Plus Abs B
# ------------------------
# Python's operator module contains two-argument functions such as add and sub for Python's built-in arithmetic operators. For example, add(2, 3) evalutes to 5, just like the expression 2 + 3.

# Fill in the blanks in the following function to add a to the absolute value of b, without calling the abs function. You may not modify any of the provided code other than the two blanks.
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub     # `f` should be a function object (like `sub` or `add`) that can later be called with `a` and `b` as arguments
    else:
        f = add     # likewise
    return f(a, b)

def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


# Q2: Two of Three
# ------------------------
# Write a function that takes three positive numbers as arguments and returns the sum of the squares of the two smallest numbers. Use only a single line for the body of the function.
def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return i ** 2 + j ** 2 + k ** 2 - max(i, j, k) ** 2

def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.



# Q3: Largest Factor
# ------------------------
# Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factors are 1, 13
    1
    """
    "*** YOUR CODE HERE ***"
    k = n - 1       # counter
    while k >= 1:
        if n % k == 0:
            return k
        else:
            k -= 1



# Q4: Hailstone
# ------------------------
# Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

#   1. Pick a positive integer n as the start.
#   2. If n is even, divide it by 2.
#   3. If n is odd, multiply it by 3 and add 1.
#   4. Continue this process until n is 1.
# The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried—nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

# This sequence of values of n is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    count = 1       # counter

    while n > 0:
        if n == 1:
            print(n)
            return count    # function call termination
        else:
            if n % 2 == 0:
                print(n)
                n = n // 2
            else:
                print(n)
                n = 3 * n + 1
            count += 1
    return count

'''better than mine

def hailstone(n):
    count = 1
    print(n)
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        count += 1
    
    return count
'''