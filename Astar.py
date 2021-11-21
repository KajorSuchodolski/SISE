import datetime
from Node import Node
from functions import get_position


class Astar:
    def __init__(self, starting_board, goal_board, method):
        self.starting_board = starting_board
        self.goal_board = goal_board
        self.method = method

    def check_distance(self, node):
        score = 0
        size = len(node.board) * len(node.board[0])

        if self.method == 'hamm':
            for value in range(size - 1):
                current_row, current_column = get_position(value, node.board)
                goal_row, goal_column = get_position(value, self.goal_board)
                score += abs(goal_row - current_row) + abs(goal_column - current_column)
            return score
        else:
            for value in range(size - 1):
                current_row, current_column = get_position(value, node.board)
                goal_row, goal_column = get_position(value, self.goal_board)
                if abs(goal_row - current_row) + abs(goal_column - current_column) != 0:
                    score += 1
            return score

    def a_star(self):
        directions = ['L', 'R', 'U', 'D']
        LRUD_solution_sequence = []
        parents_queue = []
        shortest_distance_equals = []
        visited_boards = []

        shortest_distance_child = None

        depth = 0
        processed_nodes_stats = 0


        start_time = datetime.datetime.now()
        root = Node(self.starting_board, None, None)
        visited_nodes_stats = 1

        if root.board == self.goal_board:
            end_time = datetime.datetime.now()
            exec_time = (end_time - start_time).total_seconds() * 1000

            LRUD_solution_sequence = None
            solution_length = 0

            print('Solution found')

            return LRUD_solution_sequence, solution_length, depth, exec_time, visited_nodes_stats, processed_nodes_stats

        else:
            parents_queue.append(root)
            shortest_distance = self.check_distance(root)
            visited_boards.append(root.board)
            processed_nodes_stats += 1

        while parents_queue:
            depth += 1
            shortest_distance_equals.clear()

            for parent in parents_queue:
                for direction in directions:
                    child = parent.create_one_child(direction)
                    if child is not None:
                        child_distance = self.check_distance(child)

                        if child.board in visited_boards:
                            visited_nodes_stats += 1

                        elif child.board not in visited_boards and child_distance < shortest_distance:
                            shortest_distance = child_distance
                            shortest_distance_child = child
                            shortest_distance_equals.append(child)
                            visited_boards.append(child.board)

                            processed_nodes_stats += 1
                            visited_nodes_stats += 1

            parents_queue.clear()

            if shortest_distance != 0:
                if len(shortest_distance_equals) > 1:
                    for equal in shortest_distance_equals:
                        parents_queue.append(equal)
                else:
                    parents_queue.append(shortest_distance_child)
            else:
                end_time = datetime.datetime.now()
                exec_time = (end_time - start_time).total_seconds() * 1000

                while shortest_distance_child:
                    if shortest_distance_child.direction is not None:
                        LRUD_solution_sequence.append(shortest_distance_child.direction)
                    shortest_distance_child = shortest_distance_child.parent_node
                LRUD_solution_sequence.reverse()
                solution_length = len(LRUD_solution_sequence)

                print('Solution found')

                return LRUD_solution_sequence, solution_length, depth, exec_time,\
                       visited_nodes_stats, processed_nodes_stats

        end_time = datetime.datetime.now()
        exec_time = (end_time - start_time).total_seconds() * 1000

        solution_length = -1
        LRUD_solution_sequence = None

        print('Solution not found')

        return LRUD_solution_sequence, solution_length, depth, exec_time, visited_nodes_stats, processed_nodes_stats