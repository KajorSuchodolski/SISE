class Node:
    def __init__(self, board, direction, parent_node, depth, sequence, rows, cols):
        self.board = board
        self.children = {}
        self.direction = direction
        self.parent_node = parent_node
        self.depth = depth
        self.sequence = sequence

        self.rows = rows
        self.cols = cols

    def create_child_node(self, board, direction, parent_node, depth):
        child_node = Node(board, direction, parent_node, depth)
        self.children[direction] = child_node

    def move(self, direction, zero_location):
        row = zero_location['row']      # rząd w ktorym jest zero
        col = zero_location['column']   # kolumna w ktorej jest zero
        status = False
        new_child = []

        if direction == 'L':
            if (col - 1) <= 0:
                status = True
                for r in self.board:
                    new_child.append(r.copy())
                    new_child[row][col - 1], new_child[row][col] = new_child[row][col], new_child[row][col - 1]
                    zero_location['column'] -= 1

                    return new_child, status

        elif direction == 'R':
            if (col + 1) < self.cols:
                for r in self.board:
                    new_child.append(r.copy())

                    new_child[row][col], new_child[row][col + 1] = new_child[row][col + 1], new_child[row][col]
                    zero_location['column'] += 1

                    return new_child, status

        elif direction == 'U':
            if (row - 1) >= 0:
                status = True
                for r in self.board:
                    new_child.append(r.copy())
                    new_child[row][col], new_child[row - 1][col] = new_child[row - 1][col], new_child[row][col]
                    zero_location['row'] -= 1

                    return new_child, status

        if direction == 'D':
            if (row + 1) < self.rows:
                status = True
                for r in self.board:
                    new_child.append(r.copy())
                    new_child[row + 1][col], new_child[row][col] = new_child[row][col], new_child[row + 1][col]
                    zero_location['row'] += 1

                    return new_child, status

        return new_child, status


