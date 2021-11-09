ZERO_POSITION = [[]]
ROWS, COLS = None, None


def create_fifteen_table(config):
    with open(config, 'r') as f:
        values = f.readline()
        values = values.strip()
        values = values.split(" ")
        values = list(map(int, values))
        global ROWS
        global COLS
        ROWS, COLS = values[0], values[1]
        board = []

        for i in range(0, ROWS):
            row = []
            lines = f.readline()
            lines = lines.strip()
            lines = lines.split(" ")
            lines = list(map(int, lines))

            for j in range(0, COLS):
                row.append(lines[j])
            board.append(row)

        return ROWS, COLS, board


def create_goal_board(w, k):      # tworzy tablice docelową
    goal_board = []
    numbers = []

    for i in range(1, w * k):
        numbers.append(i)
    numbers.append(0)

    numbers_iter = iter(numbers)

    for i in range(0, w):
        row = []
        for j in range(0, k):
            row.append(next(numbers_iter))

        goal_board.append(row)

    return goal_board


def get_empty_field(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 0:
                return i, j

