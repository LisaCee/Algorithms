#!/usr/bin/python

import sys


def recurse(prev, n):
    if n == 0:
        return prev
    rock_move = recurse(prev + ['rock'], n-1)
    paper_move = recurse(prev + ['paper'], n-1)
    scissors_move = recurse(prev + ['scissors'], n-1)
    return [rock_move, paper_move, scissors_move]


def rock_paper_scissors(n):
    results = recurse([], n)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
