"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls > 0, "Must roll at least once."
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # to keep track of numbers
    total = 0
    found_one = False   # to track if any roll was 1
    num_of_loops = 0

    while num_of_loops < num_rolls:
        result = dice()
        if result == 1:
            found_one = True
        total += result
        num_of_loops += 1   # I forgot this

    if found_one == True:
        return 1
    else:
        return total
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored when the current player rolls 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    result = 0
    oppo_tens = (opponent_score // 10) % 10
    play_ones = player_score % 10
    total = 3 * abs(oppo_tens - play_ones)

    if total == 0:
        result = 1
    else:
        result = total
    return result
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    current player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, "num_rolls must be an integer."
    assert num_rolls >= 0, "Cannot roll a negative number of dice in take_turn."
    assert num_rolls <= 10, "Cannot roll more than 10 dice."
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    result = 0
    if num_rolls == 0:
        result = boar_brawl(player_score, opponent_score)
    else:
        result = roll_dice(num_rolls, dice)
    return result
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True


def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    candidate_of_factors = 1
    num_of_factors = 0
    while candidate_of_factors <= n:
        if n % candidate_of_factors == 0:
            num_of_factors += 1
        candidate_of_factors += 1
    return num_of_factors
    # END PROBLEM 4


def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    factors = num_factors(score)
    if factors == 3 or factors == 4:
        n = score + 1
        while True:
            if is_prime(n): # is_prime returns True/False
                return n
            n += 1
    else:
        return score # return original score is not sus
    # END PROBLEM 4


def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    turn_points = take_turn(num_rolls, player_score, opponent_score, dice)

    new_score = player_score + turn_points

    final_score = sus_points(new_score)
    return final_score


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update, score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            num_rolls = strategy0(score0, score1)
            score0 = update(num_rolls, score0, score1, dice)
        else:
            num_rolls = strategy1(score1, score0)
            score1 = update(num_rolls, score1, score0, dice)
        who = 1 - who
    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10

    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    def strategy(score, opponent_score):
        return n
    return strategy
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    for every possible combination of score and opponent_score
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    first_result = strategy(0, 0)

    score = 0
    while score < goal:
        opponent_score = 0
        while opponent_score < goal:
            if strategy(score, opponent_score) != first_result:
                return False
            opponent_score += 1
        score += 1
    return True
    # END PROBLEM 7


def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """

    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def averaged_function(arg1=None, arg2=None):
        total = 0
        count = 0
        while count < times_called:
            if arg1 is None:
                total += original_function()
            elif arg2 is None:
                total += original_function(arg1)
            else:
                total += original_function(arg1, arg2)
            count += 1
        return total / times_called
    return averaged_function
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    best_score = 0
    best_num_rolls = 1
    
    num_rolls = 1
    while num_rolls <= 10:
        averaged_roll = make_averaged(roll_dice, times_called)
        average_score = averaged_roll(num_rolls, dice)
        
        if average_score > best_score:
            best_score = average_score
            best_num_rolls = num_rolls
        
        num_rolls += 1
    
    return best_num_rolls
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print("Max scoring num rolls for six-sided dice:", six_sided_max)

    print("always_roll(6) win rate:", average_win_rate(always_roll(6)))  # near 0.5
    print("catch_up win rate:", average_win_rate(catch_up))
    print("always_roll(3) win rate:", average_win_rate(always_roll(3)))
    print("always_roll(8) win rate:", average_win_rate(always_roll(8)))

    print("boar_strategy win rate:", average_win_rate(boar_strategy))
    print("sus_strategy win rate:", average_win_rate(sus_strategy))
    print("final_strategy win rate:", average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"




def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore the Sus Fuss rule.
    """
    # BEGIN PROBLEM 10
    """return num_rolls  # Remove this line once implemented."""
    if boar_brawl(score, opponent_score) >= threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when rolling 0 increases the score by at least
    THRESHOLD points, and returns NUM_ROLLS otherwise. Consider both the Boar Brawl and
    Suss Fuss rules."""
    # BEGIN PROBLEM 11
    """return num_rolls  # Remove this line once implemented."""
    # Calculate what the new score would be if we roll 0 dice
    new_score = sus_update(0, score, opponent_score)
    score_increase = new_score - score
    
    if score_increase >= threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    
    This strategy combines Sus Fuss and Boar Brawl advantages:
    1. Use sus_strategy with threshold 8 as primary decision
    2. If close to winning (within 10 points), be more conservative
    3. If far behind (>20 points), take more risks
    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    """return 6  # Remove this line once implemented."""
    # Check if we can win with Boar Brawl or low-risk rolling
    points_to_win = 100 - score
    
    # If very close to winning, be conservative
    if points_to_win <= 10:
        boar_points = sus_update(0, score, opponent_score) - score
        if boar_points >= points_to_win:
            return 0  # Win with Boar Brawl
        else:
            return 4  # Safe roll
    
    # If far behind, take more risks
    if score < opponent_score - 20:
        return sus_strategy(score, opponent_score, threshold=6, num_rolls=8)
    
    # Normal play: use sus_strategy with moderate threshold
    return sus_strategy(score, opponent_score, threshold=8, num_rolls=6)
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument(
        "--run_experiments", "-r", action="store_true", help="Runs strategy experiments"
    )

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()