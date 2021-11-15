from BFS import BFS
from Astar import Astar
from functions import zero_init, create_goal_board, create_fifteen_table

ORIGINAL_BOARD = [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 11, 8], [13, 14, 15, 12]]
SEQUENCE = ['R', 'U', 'L', 'D']


test = create_fifteen_table("4x4_01_0001.txt")
ORIGINAL_BOARD = test[0]

zero_init(ORIGINAL_BOARD)
GOAL = create_goal_board(4, 4)

bfs = BFS(ORIGINAL_BOARD, GOAL, SEQUENCE)
bfs_algorithm_solution = bfs.bfs_algorithm()[0]
print(bfs_algorithm_solution)

a_star_manh = Astar(ORIGINAL_BOARD, GOAL, "hamm")
print(a_star_manh.a_star())


