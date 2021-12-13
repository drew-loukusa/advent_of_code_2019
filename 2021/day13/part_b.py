# https://adventofcode.com/2021/day/13

import sys
from copy import deepcopy
from collections import defaultdict as dd
from aocd.models import Puzzle
from my_aoc_utils.utils import save_puzzle, AOC_Test
from part_a import process, solve, Dot, dump_dots

def main(infile):
    return solve(*process(infile))
    
if __name__ == "__main__":
    year, day = 2021, 13
    save_puzzle(year, day, __file__)
    aoc = AOC_Test(main, __file__)

    # Run question 
    aoc.test("day13.txt", ans=-1, save_answer=True)

    # Submit if user passed in 'submit' on command line
    if len(sys.argv) > 1 and sys.argv[1] == "submit":
        puzzle = Puzzle(year=year, day=day)
        puzzle.answer_a = aoc.answer