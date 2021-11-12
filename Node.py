from functions import ZERO_POSITION, zero_init


class Node:
    def __init__(self, board, direction, parent_node, LRUD_sequence):
        self.board = board
        self.children = {}
        self.direction = direction
        self.parent_node = parent_node
        self.LRUD_sequence = LRUD_sequence.copy()  # for DFS

    def create_one_child(self, direction, LRUD_sequence):
        new_board = self.move(direction)
        if new_board is not None:
            node = Node(new_board, direction, self, LRUD_sequence)
            return node
        else:
            return None         # jesli pozycja zera nie spelnia warunkow do stworzenia dziecka - zwraca None

    def move(self, direction):
        zero_init(self.board)
        row_zero = ZERO_POSITION[0]   # rząd w ktorym jest zero
        col_zero = ZERO_POSITION[1]   # kolumna w ktorej jest zero

        if direction == 'L':
            if (col_zero - 1) >= 0:
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero][col_zero - 1], new_board[row_zero][col_zero] \
                    = new_board[row_zero][col_zero], new_board[row_zero][col_zero - 1]

                ZERO_POSITION[1] -= 1

                return new_board

        elif direction == 'R':
            if (col_zero + 1) < len(self.board[0]):
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero][col_zero], new_board[row_zero][col_zero + 1]\
                    = new_board[row_zero][col_zero + 1], new_board[row_zero][col_zero]

                ZERO_POSITION[1] += 1

                return new_board

        elif direction == 'U':
            if (row_zero - 1) >= 0:
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero][col_zero], new_board[row_zero - 1][col_zero]\
                    = new_board[row_zero - 1][col_zero], new_board[row_zero][col_zero]

                ZERO_POSITION[0] -= 1

                return new_board

        if direction == 'D':
            if (row_zero + 1) < len(self.board):
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero + 1][col_zero], new_board[row_zero][col_zero] \
                    = new_board[row_zero][col_zero], new_board[row_zero + 1][col_zero]

                ZERO_POSITION[0] += 1

                return new_board

        return None

    def pop_LRUD_element(self):
        self.LRUD_sequence.pop(0)
