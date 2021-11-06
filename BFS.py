from Node import Node


class BFS:
    def __init__(self, starting_board, strategy_parameter, goal_board, rows, cols, zero_loc):
        self.starting_board = starting_board
        self.strategy_parameter = strategy_parameter
        self.goal_board = goal_board

        self.rows = rows
        self.cols = cols
        self.zero_loc = zero_loc

    def create_nodes_level(self, node):     # tworzenie
        possible_solutions = {}

        for s in self.strategy_parameter:
            new_child = node.move(s, self.zero_loc)[0]
            status = node.move(s, self.zero_loc)[1]
            if status:
                possible_solutions[s] = new_child

        return possible_solutions  # zwraca nam np zestaw {'L': nowa_tablica, 'R': nowa_tablica2}

    def bfs_algorithm(self):
        new_node = Node()
        list_solutions = []

        while True:
            possible_solutions = self.create_nodes_level(new_node)
            list_solutions.append(possible_solutions)

            for p in possible_solutions.values():
                if p == self.goal_board:
                    return possible_solutions.keys()  # tablica taka sama jak wzorcowa -> bierzemy ten zestaw 'L','R','L','U'...










