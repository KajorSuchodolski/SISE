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
        new_child = []
        row = zero_location['row']
        col = zero_location['column']

        if direction == 'L':
            if (col - 1) in range(0, self.cols):
                status = True
                for r in self.board:
                    new_child.append(r.copy())
                    new_child[row][col - 1], new_child[row][col] = new_child[row][col], new_child[row][col - 1]
                    zero_location['column'] -= 1

                    # self.create_child_node(new_child, move)
                    return new_child, status

        elif direction == 'R':
            if (col + 1) in range(0, self.cols):
                for r in self.board:
                    new_child.append(r.copy())

                    new_child[row][col], new_child[row][col + 1] = new_child[row][col + 1], new_child[row][col]
                    zero_location['column'] += 1
                    # self.create_child(tmp_array, move)




