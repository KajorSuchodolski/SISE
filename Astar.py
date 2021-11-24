from functions import get_position
from Node import Node


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

    def compute_cost_g(self, node):
        cost = 0
        while node:
            node = node.parent_node
            cost += 1

        return cost

    def calculate_f_value(self, node):
        g = self.compute_cost_g(node)
        h = self.compute_manhattan_h(node)

        return g + h


    def solve(self):
        parents_pool = []
        visited_boards = []

        visited_nodes_stats = 0
        processed_nodes_stats = 0
        moves_sequence = ['L', 'R', 'U', 'D']

        root = Node(self.starting_board, None, None, None)
        root.distance = self.calculate_f_value(root)
        if root.distance == 0:
            print('Solution found.')

        parents_pool.append(root)

        while parents_pool:
            parents_pool.sort(key=lambda x: x.distance)
            current_parent = parents_pool.pop(0)


            print("GÓWNO")
            for parent in parents_pool:
                print(str(parent) + "z chujowym dystansem: " + str(parent.distance))

            if current_parent.distance == 0:
                print('Solfound')
                return
            children = []
            for direction in moves_sequence:
                child = current_parent.create_one_child(direction)

                if child is not None:
                    children.append(child)
                    if child.board in visited_boards:
                        visited_nodes_stats += 1

                    else:
                        child.distance = self.calculate_f_value(child)
                        parents_pool.append(child)


            visited_boards.append(current_parent.board)

            processed_nodes_stats += 1
            visited_nodes_stats += 1

        print('No solution found')

        return None