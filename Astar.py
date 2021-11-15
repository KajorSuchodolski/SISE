from Node import Node
from functions import get_position


class Astar:
    def __init__(self, starting_board, goal_board, method):
        self.starting_board = starting_board
        self.goal_board = goal_board
        self.method = method

        self.

    def manhattan_distance(self, node):
        score = 0
        size = len(node.board) * len(node.board[0])

        if self.method == 'manh':
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
        shortest_distance_child = None
        shortest_distance_equals = []
        visited_boards = []

        root = Node(self.starting_board, None, None)

        if root.board == self.goal_board:
            print('Solution found')
            return 'yes'
        else:
            parents_queue.append(root)
            shortest_distance = self.manhattan_distance(root)
            visited_boards.append(root.board)

        while parents_queue:
            shortest_distance_equals.clear()

            for parent in parents_queue:
                for direction in directions:
                    child = parent.create_one_child(direction)
                    if child is not None:
                        child_distance = self.manhattan_distance(child)

                        if child_distance < shortest_distance and child.board not in visited_boards:
                            shortest_distance = child_distance
                            shortest_distance_child = child
                            shortest_distance_equals.append(child)
                            visited_boards.append(child.board)

            parents_queue.clear()

            if shortest_distance != 0:
                if len(shortest_distance_equals) > 1:
                    for equal in shortest_distance_equals:
                        parents_queue.append(equal)
                else:
                    parents_queue.append(shortest_distance_child)
            else:
                print('Solution found')
                while shortest_distance_child:
                    if shortest_distance_child.direction is not None:
                        LRUD_solution_sequence.append(shortest_distance_child.direction)
                    shortest_distance_child = shortest_distance_child.parent_node
                LRUD_solution_sequence.reverse()

                return LRUD_solution_sequence


        print('Solution not found')