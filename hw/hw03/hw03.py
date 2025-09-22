SOURCE_FILE = __file__
# --------------------------------------------
# Q1: Num Eights

def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"

    """Returns the number of 8's in the decimal representation of n."""
    if n < 10:  # base case
        return last_digit(n)
    else:       # recursive case
        return num_eights(n // 10) + last_digit(n)

def last_digit(n):
    """Return 1 if the last digit of n is 8, else 0."""
    if n % 10 == 8:
        return 1
    else:
        return 0
    
# --------------------------------------------
# Q2:Digit Distance

def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    # Base Case
    if n < 10:      
        return 0

    # Recursive Case
    last = n % 10
    second_last = (n // 10) % 10
    return abs(last - second_last) + digit_distance(n // 10)

# --------------------------------------------
# Q3: Interleaved Sum

def interleaved_sum(n, f_odd, f_even):
    """Compute the sum f_odd(1) + f_even(2) + f_odd(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    "*** YOUR CODE HERE ***"
    def odd_helper(k):
        # Base Case
        if k > n:
            return 0
        else:
            # Recursive Call
            return f_odd(k) + even_helper(k + 1)

    def even_helper(k):
        # Base Case
        if k > n:
            return 0
        else:
            # Recursive Call
            return f_even(k) + odd_helper(k + 1)
        
    return odd_helper(1)    # start the recursion from 1, which is odd

# --------------------------------------------
# Q4: Count Dollars

def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill == 100:
        return 50
    if bill == 50:
        return 20
    if bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1

def count_dollars(total):
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    bill = 100

    def constrained_count(new_total, largest_bill):
        if new_total == 0:          # Base Case: Successfully made change.
            return 1
        elif new_total < 0:         # Base Case: Overshot the total or ran out of bills.
            return 0
        elif largest_bill == None:  # Base Case: Overshot the total or ran out of bills.
            return 0
        else:                       # Recursive Call
            return constrained_count(new_total - largest_bill, largest_bill) + constrained_count(new_total, next_smaller_dollar(largest_bill))
    
    return constrained_count(total, bill)


def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100

def count_dollars_upward(total):
    """Return the number of ways to make change using bills.

    >>> count_dollars_upward(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars_upward(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars_upward(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars_upward(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars_upward(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars_upward(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_dollars_upward', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'

