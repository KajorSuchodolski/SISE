from Node import Node
from functions import get_position


class AStar:
    def __init__(self, starting_board, goal_board):
        self.starting_board = starting_board
        self.goal_board = goal_board

    def manhattan_distance(self, node):
        score = 0
        size = len(node.board) * len(node.board[0])

        for value in range(size - 1):
            current_row, current_column = get_position(value, node.board, False)
            goal_row, goal_column = get_position(value, self.goal_board, False)
            score += abs(goal_row - current_row) + abs(goal_column - current_column)
        return score

    def a_star(self):
        directions = ['L', 'R', 'U', 'D']
        parents_queue = []
        shortest_distance = 0

        root = Node(self.starting_board, None, None, ['a_star'])

        if root.board == self.goal_board:
            print('Solution found')
            return 'yes'
        else:
            parents_queue.append(root)

        while parents_queue:
            for parent in parents_queue:
                for direction in directions:
                    child = parent.create_one_child(direction, ['a_star'])
                    if self.manhattan_distance(child) < shortest_distance:
                        shortest_distance = child


