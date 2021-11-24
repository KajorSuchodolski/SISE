from functions import get_position
from Node import Node
import collections


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

    def state(self, node):
        return str(node)

    def calculate_f_value(self, node):
        g = self.compute_cost_g(node)
        h = self.compute_manhattan_h(node)

        return g + h


    def solve(self):
        # parents_pool = []
        visited_boards = []

        visited_nodes_stats = 0
        processed_nodes_stats = 0
        moves_sequence = ['L', 'R', 'U', 'D']

        root = Node(self.starting_board, None, None, None)
        root.distance = self.calculate_f_value(root)
        if root.board == self.goal_board:
            print('Solution found.')

        # parents_pool.append(root)
        parents_pool = collections.deque([root])
        seen = set()
        seen.add(self.state(parents_pool[0]))

        while parents_pool:
            # parents_pool.sort(key=lambda x: x.distance)
            # current_parent = parents_pool.pop(0)

            collections.deque(sorted(list(parents_pool), key=lambda node: node.distance))
            current_parent = parents_pool.popleft()

            print("GÓWNO")
            for parent in parents_pool:
                print(str(parent) + "z chujowym dystansem: " + str(parent.distance))

            if current_parent.board == self.goal_board:
                print('Solfound')
                return

            for direction in moves_sequence:
                child = current_parent.create_one_child(direction)

                if child is not None:
                    # if child.board in visited_boards:
                    # if child.board in seen:
                    if self.state(child) in seen:
                        visited_nodes_stats += 1

                    else:
                        child.distance = self.calculate_f_value(child)
                        parents_pool.appendleft(child)
                        # seen.add(self.state(child))
                        # visited_boards.append(child.board)

            # visited_boards.append(current_parent.board)
            seen.add(self.state(current_parent))


            processed_nodes_stats += 1
            visited_nodes_stats += 1

        print('No solution found')

        return None