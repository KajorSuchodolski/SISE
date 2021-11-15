from functions import ZERO_POSITION, zero_init


class Node:
    def __init__(self, board, direction, parent_node):
        self.board = board
        self.children = {}
        self.direction = direction
        self.parent_node = parent_node
        # self.lrud_sequence = lrud_sequence.copy()

    def create_one_child(self, direction):
        new_board = self.move(direction)
        if new_board is not None:
            node = Node(new_board, direction, self)
            return node
        else:
            return None         # jesli pozycja zera nie spelnia warunkow do stworzenia dziecka - zwraca None

    def move(self, direction, flag=False):
        zero_init(self.board)
        row_zero = ZERO_POSITION[0]   # rząd w ktorym jest zero
        col_zero = ZERO_POSITION[1]   # kolumna w ktorej jest zero

        if direction == 'L':
            if (col_zero - 1) >= 0:
                if flag:
                    return True
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero][col_zero - 1], new_board[row_zero][col_zero] \
                    = new_board[row_zero][col_zero], new_board[row_zero][col_zero - 1]

                ZERO_POSITION[1] -= 1

                return new_board

        elif direction == 'R':
            if (col_zero + 1) < len(self.board[0]):
                if flag:
                    return True
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero][col_zero], new_board[row_zero][col_zero + 1]\
                    = new_board[row_zero][col_zero + 1], new_board[row_zero][col_zero]

                ZERO_POSITION[1] += 1

                return new_board

        elif direction == 'U':
            if (row_zero - 1) >= 0:
                if flag:
                    return True
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero][col_zero], new_board[row_zero - 1][col_zero]\
                    = new_board[row_zero - 1][col_zero], new_board[row_zero][col_zero]

                ZERO_POSITION[0] -= 1

                return new_board

        elif direction == 'D':
            if (row_zero + 1) < len(self.board):
                if flag:
                    return True
                new_board = []
                for row in self.board:
                    new_board.append(row.copy())

                new_board[row_zero + 1][col_zero], new_board[row_zero][col_zero] \
                    = new_board[row_zero][col_zero], new_board[row_zero + 1][col_zero]

                ZERO_POSITION[0] += 1

                return new_board

        return None

    # def pop_LRUD_element(self):
    #     self.lrud_sequence.pop(0)

    # def remove_moves_two(self):
    #     if self.direction != 'Root Node':
    #         if self.direction == 'L':
    #             self.lrud_sequence.remove('R')
    #         if self.direction == 'R':
    #             self.lrud_sequence.remove('L')
    #         if self.direction == 'U':
    #             self.lrud_sequence.remove('D')
    #         if self.direction == 'D':
    #             self.lrud_sequence.remove('U')