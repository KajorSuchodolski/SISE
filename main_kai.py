from BFS import BFS
from functions import zero_init

ORIGINAL_BOARD = [[0, 1, 2, 7], [8, 9, 12, 10], [13, 3, 6, 4], [15, 14, 11, 5]]
TO_SOLVE = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
SEQUENCE = ['L', 'U', 'R', 'D']

zero_init(TO_SOLVE)
bfs = BFS(ORIGINAL_BOARD, TO_SOLVE, SEQUENCE)
bfs_algorithm_solution = bfs.bfs_algorithm()[0]
print(bfs_algorithm_solution)


