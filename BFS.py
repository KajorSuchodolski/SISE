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
        visited_boards = []

        LRUD_solution_sequence = []
        solution_length = 0
        depth = 0
        processed_nodes_stats = 0

        start_time = datetime.datetime.now()
        root = Node(self.starting_board, None, None)
        visited_nodes_stats = 1

        if root.board == self.goal_board:
            print('Solution found')

            end_time = datetime.datetime.now()
            exec_time = (end_time - start_time).total_seconds() * 1000
            LRUD_solution_sequence = None

            return LRUD_solution_sequence, solution_length, depth, exec_time, visited_nodes_stats, processed_nodes_stats

        else:
            parents_queue.append(root)
            visited_boards.append(root.board)
            processed_nodes_stats += 1

        while parents_queue:
            depth += 1
            for parent in parents_queue:   # kazdy wezel z glebokosci
                for direction in self.LRUD_bfs_sequence:
                    child = parent.create_one_child(direction)

                    if child is not None:
                        if child.board in visited_boards:
                            visited_nodes_stats += 1
                        else:
                            children_queue.append(child)  # kolejka dzieci kazdego wezla ktore nie zwrocily none
                            processed_nodes_stats += 1
                            visited_nodes_stats += 1

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

                    return LRUD_solution_sequence, solution_length, depth, exec_time, \
                           visited_nodes_stats, processed_nodes_stats

                else:
                    parents_queue.append(child)
                    visited_boards.append(child.board)

            children_queue.clear()


        end_time = datetime.datetime.now()
        exec_time = (end_time - start_time).total_seconds() * 1000

        solution_length = -1
        LRUD_solution_sequence = []

        return LRUD_solution_sequence, solution_length, depth, exec_time, visited_nodes_stats, processed_nodes_stats