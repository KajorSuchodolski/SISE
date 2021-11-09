import argparse
import itertools
from Board import Board
from BFS import BFS
from functions import create_fifteen_table, create_goal_board

# def parse():
#     parser = argparse.ArgumentParser(description='Arguments for the Fifteen solver')
#     parser.add_argument('strategy', type=str, help='Choose problem solving strategy')
#     parser.add_argument('strategy_parameter', type=str, help='Choose strategy parameter')
#     parser.add_argument('start_textfile', type=str, help='Add the start file')
#
#     config = parser.parse_args()
#
#     if config.strategy not in ('bfs', 'dfs', 'astr'):
#         raise Exception('Wrong strategy choice')
#
#     if (config.strategy == 'bfs' or config.strategy == 'dfs')\
#             and config.strategy_parameter not in itertools.permutations('RLUD', 4):
#         raise Exception('Wrong strategy parameter choice for bfs/dfs parameter')
#
#     if config.strategy == 'astr' and config.strategy_parameter not in ('hamm', 'manh'):
#         raise Exception('Wrong strategy parameter choice for astr parameter')
#
#     if config.start_textfile[-4] != ".txt":
#         raise Exception('Wrong format')
#
#     return config


def create_fifteen_table(config):
    with open(config, 'r') as f:
        values = f.readline()
        values = values.strip()
        values = values.split(" ")
        values = list(map(int, values))
        x = values[0]
        y = values[1]

        board = []

        for i in range(0, x):
            row = []
            lines = f.readline()
            lines = lines.strip()
            lines = lines.split(" ")
            lines = list(map(int, lines))
            for j in range(0, y):
                row.append(lines[j])
            board.append(row)

        return x, y, board


def create_goal_board(w, k):
    goal_board = []
    numbers = []

    for i in range(1, w * k):     # create a list of numbers 1...w*k and append 0
        numbers.append(i)
    numbers.append(0)

    numbers_iter = iter(numbers)

    for i in range(0, w):
        row = []
        for j in range(0, k):
            row.append(next(numbers_iter))

        goal_board.append(row)

    return goal_board


def main():
    # board = Board(5, 5)


    strategy_parameter = ['L', 'R', 'D', 'U'] # sample parameter

    rows, cols = create_fifteen_table('input.txt')[0], create_fifteen_table('input.txt')[1]
    goal_board = create_goal_board(rows, cols)

    initial_board = create_fifteen_table('input.txt')[2]
    print(initial_board)











main()