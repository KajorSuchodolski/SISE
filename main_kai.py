from BFS import BFS
from functions import zero_init, create_goal_board

ORIGINAL_BOARD = [[0, 1], [3, 2]]
GOAL = [[1, 2], [3, 0]]
SEQUENCE = ['L', 'U', 'R', 'D']

ORIGINAL_BOARD2 = [[1, 3, 4, 8], [5, 2, 7, 0], [9, 6, 11, 12], [13, 10, 14, 15]]

zero_init(ORIGINAL_BOARD2)
GOAL2 = create_goal_board(4, 4)

bfs = BFS(ORIGINAL_BOARD2, GOAL2, SEQUENCE)
bfs_algorithm_solution = bfs.bfs_algorithm()[0]
print(bfs_algorithm_solution)


