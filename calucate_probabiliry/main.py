import argparse
import getopt
import math
import sys
from scipy.special import comb, perm


def main(args):
    """
    This function is the main function to collect the input parameters.

    Args:
           args (list): collect the command and the valve.

    Returns:
           bool: True if successful, False otherwise.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    process(**vars(parser.parse_args(args)))
    return True


def process(n=None):
    """
    This function will be the number entered in the probability_of_lose 
    function, and this function check the parameter n is bigger than 0  or not.

    Args:
           n: the times of the toss coins.

    """
    # transfer the type of input parameter from string into int.
    n = int(n)
    # check the times of toss coins is bigger than zero.
    if n == 0:
        prob_of_lose = 0
    elif n < 0:
        print('n cannot small than 0.')
    else:
        prob_of_lose = probaility_of_loss(n)
        print('prob_lose=', prob_of_lose)
    pass


def probaility_of_loss(n):
    """
    This function calculates the probability of lose for toss n times coins.

    Args:
           n (int): times of toss coins.

    Returns:
            prob_of_lose(float): the probability of lose.

    """
    # parameter setting
    # head:  the gain how much we win.
    # tail:  the loss how much we lose.
    # num_of_tail: the total number of toss the tail.
    head = 12
    tail = -10
    num_of_tail = 0

    for i in range(n):
        # calucate the total gain we get
        gain = head*i + tail*(n-i)
        # if the gain is bigger than 0, it means this situation wins the game. So, quite the for loop.
        if gain > 0:
            break
        # sum the total number of loss situations.
        num_of_tail = num_of_tail + comb(n, n-i)
    # calculate the probability of loss.
    prob_of_lose = round(num_of_tail/pow(2, n), 2)
    return prob_of_lose


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
