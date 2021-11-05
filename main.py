import argparse
import itertools


def parse():
    parser = argparse.ArgumentParser(description='Arguments for the Fifteen solver')
    parser.add_argument('strategy', type=str, help='Choose problem solving strategy')
    parser.add_argument('strategy_parameter', type=str, help='Choose strategy parameter')
    parser.add_argument('start_textfile', type=str, help='Add the start file')

    config = parser.parse_args()

    if config.strategy not in ('bfs', 'dfs', 'astr'):
        raise Exception('Wrong strategy choice')

    if (config.strategy == 'bfs' or config.strategy == 'dfs')\
            and config.strategy_parameter not in itertools.permutations('RLUD', 4):
        raise Exception('Wrong strategy parameter choice for bfs/dfs parameter')

    if config.strategy == 'astr' and config.strategy_parameter not in ('hamm', 'manh'):
        raise Exception('Wrong strategy parameter choice for astr parameter')



def main():
    parse()



main()


