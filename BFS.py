import datetime
from Node import Node


class BFS:
    def __init__(self, starting_board, goal_board, LRUD_bfs_sequence):
        self.LRUD_bfs_sequence = LRUD_bfs_sequence

        self.starting_board = starting_board
        self.goal_board = goal_board

    def bfs_algorithm(self):
        children_queue = []
        visited_queue = []

        LRUD_solution_sequence = []
        solution_length = 0
        depth = 0

        start_time = datetime.datetime.now()

        root = Node(self.starting_board, None, None, ['bfs'])

        if root.board == self.goal_board:
            print('Solution found')
        else:
            visited_queue.append(root)

            while visited_queue:
                for visited in visited_queue:   # kazdy wezel z glebokosci
                    for direction in self.LRUD_bfs_sequence:
                        children_queue.append(visited.create_one_child(direction)) # kolejka dzieci kazdego wezla
                    visited_queue.pop(0)

                depth += 1

                while children_queue:
                    for sibling in children_queue:
                        if sibling.board == self.goal_board:
                            print('Solution found')

                            while sibling is not None:
                                LRUD_solution_sequence.append(sibling.direction)
                                sibling = sibling.parent_node
                                solution_length += 1

                                end_time = datetime.datetime.now()
                                exec_time = (end_time - start_time).total_seconds() * 1000

                            return LRUD_solution_sequence, solution_length, depth, exec_time
                        else:
                            visited_queue.append(sibling)
                    children_queue.pop(0)

            end_time = datetime.datetime.now()
            exec_time = (end_time - start_time).total_seconds() * 1000

            solution_length = -1

        return solution_length, depth, exec_time