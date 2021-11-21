from BFS import BFS
from DFS import DFS
from Astar import Astar
from functions import create_fifteen_table, create_goal_board
import argparse
import itertools

# .\__main__.py bfs LUDR 4x4_01_0001.txt 4x4_01_0001_dfs_ludr_sol.txt 4x4_01_0001_dfs_ludr_stats.txt


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("algorithm", type=str)
    parser.add_argument("sequence", type=str)
    parser.add_argument("input", type=str)
    parser.add_argument("solution", type=str)
    parser.add_argument("stats", type=str)

    args = parser.parse_args()

    solve_board = create_fifteen_table(args.input)
    to_solve_board, rows, columns = solve_board[0], solve_board[1], solve_board[2]
    original_board = create_goal_board(rows, columns)
    if args.sequence not in ("manh", "hamm"):
        sequence = tuple(args.sequence.upper())
    elif args.sequence == "manh":
        sequence = "manh"
    else:
        sequence = "hamm"

    all_sequences = list(itertools.permutations(['L', 'R', 'U', 'D']))
    all_sequences.append('manh')
    all_sequences.append('hamm')

    if args.algorithm not in ("bfs", "dfs", "astr"):
        raise Exception("Wrong algorithm choice")
    if sequence not in all_sequences:
        raise Exception("Wrong sequence choice")


    if args.algorithm == "dfs":
        print('Doesnt work yet')
        # dfs = DFS(to_solve_board, original_board, sequence)
        # dfs.dfs()
        #
        # with open(args.solution, "w") as f_solution:
        #     if len(dfs.visited) == 0:
        #         f_solution.write("-1")
        #     else:
        #         f_solution.write(str(len(dfs.visited)) + "\n")
        #         f_solution.write(str(dfs.visited))
        #
        # with open(args.stats, "w") as f_stats:
        #     if len(dfs.visited) == 0:
        #         f_stats.write("-1")
        #     else:
        #         f_stats.write(str(len(dfs.visited)) + "\n")
        #         f_stats.write(str(dfs.visits) + "\n")
        #         f_stats.write(str(dfs.processed) + "\n")
        #         f_stats.write(str(dfs.max_depth_visited) + "\n")
        #         f_stats.write(str(round(dfs.time, 3)) + "\n")

    elif args.algorithm == "bfs":
        bfs = BFS(to_solve_board, original_board, sequence)
        result = bfs.bfs_algorithm()

        with open(args.solution, "w") as f_solution:
            f_solution.write(str(result[1]) + "\n")        # dlugosc znalezionego rozwiazania
            if result[0] is not None:
                LRUD_sequence = ''.join(map(str, result[0]))
                f_solution.write(LRUD_sequence)        # sekwencja liter

        with open(args.stats, "w") as f_stats:
            f_stats.write(str(result[1]) + "\n")       # dlugosc rozwiazania
            f_stats.write(str(result[4]) + "\n")       # liczba stanow odwiedzonych
            f_stats.write(str(result[5]) + "\n")       # liczba stanow przetworzonych
            f_stats.write(str(result[2]) + "\n")       # glebokosc
            f_stats.write(str(result[3]) + "\n")       # dlugosc procesu obliczeniowego w ms


    elif args.algorithm == "astr":
        astr = None

        if sequence == "manh":
            manh = Astar(to_solve_board, original_board, "manh")

            result = manh.a_star()

            with open(args.solution, "w") as f_solution:
                f_solution.write(str(result[1]) + "\n")  # dlugosc znalezionego rozwiazania
                if result[0] is not None:
                    LRUD_sequence = ''.join(map(str, result[0]))
                    f_solution.write(LRUD_sequence)  # sekwencja liter

            with open(args.stats, "w") as f_stats:
                f_stats.write(str(result[1]) + "\n")  # dlugosc rozwiazania
                f_stats.write(str(result[4]) + "\n")  # liczba stanow odwiedzonych
                f_stats.write(str(result[5]) + "\n")  # liczba stanow przetworzonych
                f_stats.write(str(result[2]) + "\n")  # glebokosc
                f_stats.write(str(result[3]) + "\n")  # dlugosc procesu obliczeniowego w ms

        elif sequence == "hamm":
            astr = Astar(to_solve_board, original_board, "hamm")

        # astr.a_star()





if __name__ == '__main__':
    main()
