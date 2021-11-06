class Board:
    def __init__(self, w, k):
        self.w = w
        self.k = k

    def create_goal_board(self):
        goal_board = []
        numbers = []

        for i in range(1, self.w * self.k):     # create a list of numbers 1...w*k and append 0
            numbers.append(i)
        numbers.append(0)

        numbers_iter = iter(numbers)

        for i in range(0, self.w):
            row = []
            for j in range(0, self.k):
                row.append(next(numbers_iter))

            goal_board.append(row)

        return goal_board
