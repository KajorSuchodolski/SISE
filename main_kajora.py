from DFS import DFS
from functions import zero_init, create_fifteen_table, create_goal_board

ORIGINAL_BOARD = create_goal_board(4, 4)
# TO_SOLVE = [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 11, 8], [13, 14, 15, 12]]
SEQUENCE = ['L', 'U', 'D', 'R']

test = create_fifteen_table("4x4_01_0001.txt")
TO_SOLVE = test[0]
print(TO_SOLVE)
zero_init(TO_SOLVE)
dfs = DFS(TO_SOLVE, ORIGINAL_BOARD, SEQUENCE)
dfs.dfs()
print(dfs.visited)
print(dfs.visits)
print(dfs.processed)
print(dfs.time)

