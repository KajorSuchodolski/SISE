import datetime
from Node import Node


class BFS:
    def __init__(self, starting_board, goal_board, LRUD_bfs_sequence):
        self.LRUD_bfs_sequence = LRUD_bfs_sequence

        self.starting_board = starting_board
        self.goal_board = goal_board

    def bfs_algorithm(self):
        children_queue = []
        parents_queue = []

        LRUD_solution_sequence = []
        solution_length = 0
        depth = 0
        visited_boards = []

        start_time = datetime.datetime.now()
        root = Node(self.starting_board, None, None, ['bfs'])

        if root.board == self.goal_board:
            print('Solution found')

            end_time = datetime.datetime.now()
            exec_time = (end_time - start_time).total_seconds() * 1000
            return solution_length, depth, exec_time

        else:
            parents_queue.append(root)
            visited_boards.append(root.board)

        while parents_queue:
            depth += 1
            for parent in parents_queue:   # kazdy wezel z glebokosci
                for direction in self.LRUD_bfs_sequence:
                    child = parent.create_one_child(direction, ['bfs'])
                    if child is not None and child.board not in visited_boards:
                        children_queue.append(child)  # kolejka dzieci kazdego wezla ktore nie zwrocily none

            parents_queue.clear()

            for child in children_queue:
                if child.board == self.goal_board:
                    print('Solution found')

                    while child:
                        if child.direction is not None:
                            LRUD_solution_sequence.append(child.direction)
                        child = child.parent_node
                        solution_length += 1

                    LRUD_solution_sequence.reverse()
                    end_time = datetime.datetime.now()
                    exec_time = (end_time - start_time).total_seconds() * 1000

                    return LRUD_solution_sequence, solution_length, depth, exec_time

                else:
                    parents_queue.append(child)
                    visited_boards.append(child.board)

            children_queue.clear()


        end_time = datetime.datetime.now()
        exec_time = (end_time - start_time).total_seconds() * 1000

        solution_length = -1

        return solution_length, depth, exec_time