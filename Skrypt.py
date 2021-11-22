from BFS import BFS
from functions import create_goal_board, create_fifteen_table
from openpyxl import Workbook
import csv


ORIGINAL_BOARD = create_goal_board(4, 4)

bfs_results = []
bfs_seq = [['R', 'D', 'U', 'L'], ['R', 'D', 'L', 'U'], ['D', 'R', 'U', 'L'],
           ['D', 'R', 'L', 'U'], ['L', 'U', 'D', 'R'], ['L', 'U', 'R', 'D'],
           ['U', 'L', 'D', 'R'], ['U', 'L', 'R', 'D']]


# bfs = BFS

seq = bfs_seq[7]

for i in range(1, 8):
    for j in range(0, 414):
        if 0 < j < 10:
            try:
                tmp = create_fifteen_table(
                    "C:\\Users\\Radek\\PycharmProjects\\SISE2\\input\\4x4_0" + str(i) + "_0000" + str(j) + ".txt")
                TO_SOLVE = tmp[0]
                bfs = BFS(TO_SOLVE, ORIGINAL_BOARD, seq)
                bfs_results.append(bfs.bfs_algorithm())
            except:
                continue
        elif 11 < j < 100:
            try:
                tmp = create_fifteen_table("input/4x4_0" + str(i) + "_000" + str(j) + ".txt")
                TO_SOLVE = tmp[0]
                bfs = BFS(ORIGINAL_BOARD, TO_SOLVE, seq)
                bfs_results.append(bfs.bfs_algorithm())
            except:
                continue
        elif 101 < j < 1000:
            try:
                tmp = create_fifteen_table("input/4x4_0" + str(i) + "_00" + str(j) + ".txt")
                TO_SOLVE = tmp[0]
                bfs = BFS(ORIGINAL_BOARD, TO_SOLVE, seq)
                bfs_results.append(bfs.bfs_algorithm())
            except:
                continue

with open('bfs_data_' + str(seq) + '.csv', 'w', newline='') as f_csv:
    writer = csv.writer(f_csv)
    for row in bfs_results:
        writer.writerow(row)

# with open('bfs_data_solution_length.csv', 'w', newline='') as f_csv:
#     writer = csv.writer(f_csv, delimiter=',')
#     writer.writerow('Solution length')
#     for row in bfs_results:
#         writer.writerow(str(row[1]))
#
# with open('bfs_data_depth.csv', 'w', newline='') as f_csv:
#     writer = csv.writer(f_csv, delimiter=',')
#     writer.writerow('Depth')
#     for row in bfs_results:
#         writer.writerow(str(row[2]))
#
# with open('bfs_data_exec_time.csv', 'w', newline='') as f_csv:
#     writer = csv.writer(f_csv, delimiter=',')
#     writer.writerow('Exec time')
#     for row in bfs_results:
#         writer.writerow(str(row[3]))
#
# with open('bfs_data_visited_nodes.csv', 'w', newline='') as f_csv:
#     writer = csv.writer(f_csv)
#     writer.writerow('Visited nodes')
#     for row in bfs_results:
#         writer.writerow(str(row[4]))
#
# with open('bfs_data_processed_nodes.csv', 'w', newline='') as f_csv:
#     writer = csv.writer(f_csv)
#     writer.writerow('Processed nodes')
#     for row in bfs_results:
#         writer.writerow(str(row[5]))