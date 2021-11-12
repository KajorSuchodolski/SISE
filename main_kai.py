from BFS import BFS
from functions import zero_init, create_goal_board

ORIGINAL_BOARD = [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 11, 8], [13, 14, 15, 12]]
SEQUENCE = ['L', 'U', 'R', 'D']

zero_init(ORIGINAL_BOARD)
GOAL = create_goal_board(4, 4)

bfs = BFS(ORIGINAL_BOARD, GOAL, SEQUENCE)
bfs_algorithm_solution = bfs.bfs_algorithm()[0]
print(bfs_algorithm_solution)


