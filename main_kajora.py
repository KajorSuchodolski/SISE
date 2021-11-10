from DFS import DFS
from functions import zero_init

ORIGINAL_BOARD = [[1, 2], [3, 0]]
TO_SOLVE = [[0, 1], [3, 2]]
SEQUENCE = ['U', 'R', 'L', 'D']


zero_init(TO_SOLVE)
dfs = DFS(ORIGINAL_BOARD, TO_SOLVE, SEQUENCE)
print(dfs.dfs())