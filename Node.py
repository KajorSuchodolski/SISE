from functions import ZERO_POSITION


class Node:
    def __init__(self, board, direction, parent_node):
        self.board = board
        self.children = {}
        self.direction = direction
        self.parent_node = parent_node

        # depth, sequence, rows, cols
    # def create_child_node(self, board, direction, parent_node, depth):
    #     child_node = Node(board, direction, parent_node, depth)
    #     self.children[direction] = child_node

    def create_one_child(self, parent_node, direction):
        status = parent_node.move(direction, ZERO_POSITION)[1]
        if status:
            child_board = parent_node.move(direction, ZERO_POSITION, parent_node.board)[0]
            node = Node(child_board, direction, parent_node)
            return node
        else:
            return None         # jesli pozycja zera nie spelnia warunkow do stworzenia dziecka - zwraca None

    def create_children_for_node(self, parent_node, LRUD_sequence):
        for direction in LRUD_sequence:
            child = self.create_one_child(parent_node, direction)   # tworzy dziecko - obiekt klasy Node - dla kazdego kierunku
            if child is not None:
                parent_node.children[direction] = child    # dzieci danego wezla: {'L': child1, 'R': child2....}

    def move(self, direction, zero_position, parent_node):
        row = zero_position[0]   # rząd w ktorym jest zero
        col = zero_position[1]   # kolumna w ktorej jest zero
        status = False  # zwraca true w przypadku kiedy ruch zera jest mozliwy

        if direction == 'L':
            if (col - 1) <= 0:
                status = True
                new_board = parent_node.board.copy()

                new_board[row][col - 1], new_board[row][col] = new_board[row][col], new_board[row][col - 1]
                zero_position[1] -= 1

                return new_board, status

        elif direction == 'R':
            if (col + 1) < len(self.board[0]):
                status = True
                new_board = parent_node.board.copy()

                new_board[row][col], new_board[row][col + 1] = new_board[row][col + 1], new_board[row][col]
                zero_position[1] += 1

                return new_board, status

        elif direction == 'U':
            if (row - 1) >= 0:
                status = True
                new_board = parent_node.board.copy()

                new_board[row][col], new_board[row - 1][col] = new_board[row - 1][col], new_board[row][col]
                zero_position[0] -= 1

                return new_board, status

        if direction == 'D':
            if (row + 1) < self.rows:
                status = True
                new_board = parent_node.board.copy()

                new_board[row + 1][col], new_board[row][col] = new_board[row][col], new_board[row + 1][col]
                zero_position[0] += 1

                return new_board, status

        return None
