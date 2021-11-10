from functions import ZERO_POSITION


class Node:
    def __init__(self, board, direction, parent_node, LRUD_sequence):
        self.board = board
        self.children = {}
        self.direction = direction
        self.parent_node = parent_node
        self.LRUD_sequence = LRUD_sequence.copy()  # for DFS

    def create_one_child(self, direction):
        new_board = self.move(direction, ZERO_POSITION)
        if new_board is not None:
            node = Node(new_board, direction, self, self.LRUD_sequence)
            return node
        else:
            return None         # jesli pozycja zera nie spelnia warunkow do stworzenia dziecka - zwraca None

    def move(self, direction, zero_position):
        row = zero_position[0]   # rząd w ktorym jest zero
        col = zero_position[1]   # kolumna w ktorej jest zero

        if direction == 'L':
            if (col - 1) >= 0:
                status = True
                new_board = self.board.copy()

                new_board[row][col - 1], new_board[row][col] = new_board[row][col], new_board[row][col - 1]
                zero_position[1] -= 1

                return new_board

        elif direction == 'R':
            if (col + 1) < len(self.board[0]):
                status = True
                new_board = self.board.copy()

                new_board[row][col], new_board[row][col + 1] = new_board[row][col + 1], new_board[row][col]
                zero_position[1] += 1

                return new_board

        elif direction == 'U':
            if (row - 1) >= 0:
                status = True
                new_board = self.board.copy()

                new_board[row][col], new_board[row - 1][col] = new_board[row - 1][col], new_board[row][col]
                zero_position[0] -= 1

                return new_board

        if direction == 'D':
            if (row + 1) < len(self.board):
                status = True
                new_board = self.board.copy()

                new_board[row + 1][col], new_board[row][col] = new_board[row][col], new_board[row + 1][col]
                zero_position[0] += 1

                return new_board

        return None

    def pop_LRUD_element(self):
        self.LRUD_sequence.pop(0)