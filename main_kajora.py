from DFS import DFS
from functions import get_position

ORIGINAL_BOARD = [[1, 2], [3, 0]]
TO_SOLVE = [[0, 1], [3, 2]]
SEQUENCE = ['U', 'R', 'L', 'D']


get_position(ORIGINAL_BOARD, 0, True)
dfs = DFS(ORIGINAL_BOARD, TO_SOLVE, SEQUENCE)
print(dfs.dfs())