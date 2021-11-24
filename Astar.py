from functions import get_position
from Node import Node
import collections
import operator
import datetime


class Astar:
    def __init__(self, heuristic, starting_board, goal_board):
        self.heuristic = heuristic
        self.starting_board = starting_board
        self.goal_board = goal_board

    def compute_manhattan_h(self, node):
        score = 0
        board_size = len(node.board) * len(node.board[0])

        for value in range(0, board_size - 1):
            iGoal, jGoal = get_position(value, self.goal_board)
            iActual, jActual = get_position(value, node.board)
            score += abs(iGoal - iActual) + abs(jGoal - jActual)
        return score

    def compute_hamming_h(self, node):
        # do zrobienia!

    def compute_cost_g(self, node):
        cost = 0
        while node.direction is not None:
            node = node.parent_node
            cost += 1

        return cost

    def state(self, node):
        return str(node)

    def calculate_f_value(self, node, heuristic):
        g = self.compute_cost_g(node)
        if heuristic == "manh":
            h = self.compute_manhattan_h(node)
        else:
            h = self.compute_hamming_h(node)

        return g + h


    def solve(self):
        visited_boards = []
        LRUD_astar_sequence = []
        parents_pool = []

        visited_nodes_stats = 0
        processed_nodes_stats = 0
        moves_sequence = ['L', 'R', 'U', 'D']

        start_time = datetime.datetime.now()

        root = Node(self.starting_board, None, None, None)
        root.distance = self.calculate_f_value(root)
        if root.board == self.goal_board:
            print('Solution found.')
            end_time = datetime.datetime.now()
            exec_time = (end_time - start_time).total_seconds() * 1000

            depth = 0
            solution_length = 0
            LRUD_solution_sequence = None
            return LRUD_solution_sequence, solution_length, depth, exec_time, visited_nodes_stats, processed_nodes_stats

        visited_nodes_stats += 1
        processed_nodes_stats += 1
        visited_boards.append(root.board)

        parents_pool.append(root)

        while parents_pool:
            parents_pool = sorted(parents_pool, key=operator.attrgetter('distance'))

            current_parent = parents_pool.pop(0)

            if current_parent.board == self.goal_board:
                end_time = datetime.datetime.now()
                exec_time = (end_time - start_time).total_seconds() * 1000

                LRUD_astar_sequence.append(current_parent.direction)
                depth = self.compute_cost_g(current_parent)

                while current_parent.parent_node:
                    current_parent = current_parent.parent_node
                    LRUD_astar_sequence.append(current_parent.direction)

                LRUD_astar_sequence.remove(None)

                LRUD_astar_sequence.reverse()
                solution_length = len(LRUD_astar_sequence)

                print(solution_length)
                print(depth)
                print(LRUD_astar_sequence)
                print(visited_nodes_stats)
                print(processed_nodes_stats)
                print(exec_time)

                print('Solution found.')


                return LRUD_astar_sequence, solution_length, depth, exec_time,\
                       visited_nodes_stats, processed_nodes_stats

            for direction in moves_sequence:
                child = current_parent.create_one_child(direction)

                if child is not None:
                    # if child.board in visited_boards:
                    # if child.board in seen:
                    if child.board in visited_boards:
                        visited_nodes_stats += 1

                    else:
                        child.distance = self.calculate_f_value(child, self.heuristic)
                        parents_pool.append(child)
                        # seen.add(self.state(child))
                        # visited_boards.append(child.board)

            visited_boards.append(current_parent.board)

            processed_nodes_stats += 1
            visited_nodes_stats += 1

            if len(parents_pool) == 0:
                depth_last = self.compute_cost_g(current_parent)


        end_time = datetime.datetime.now()
        exec_time = (end_time - start_time).total_seconds() * 1000

        solution_length = -1
        LRUD_solution_sequence = None

        print('No solution found.')

        return LRUD_astar_sequence, solution_length, depth_last, exec_time, visited_nodes_stats, processed_nodes_stats