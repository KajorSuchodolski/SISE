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



def main():
    strategy_parameter = ['L', 'R', 'D', 'U']

    initial_board = create_fifteen_table('input.txt')[0]
    w, k = create_fifteen_table('input.txt')[1], create_fifteen_table('input.txt')[2]

    goal_board = create_goal_board(w, k)

    print(initial_board)











main()