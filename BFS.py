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

        for s in self.strategy_parameter:           # ['L', 'R', 'U', 'D']
            status = parent.move(s, self.zero_loc)[1]
            if status:
                possible_solutions[s] = new_child

        return possible_solutions  # zwraca nam np zestaw {'L': [nowa_tablica, poprzednik] 'R': [nowa_tablica2, poprzednik]}

    def bfs_algorithm(self):
        root = Node(self.starting_board, self.parent_node, self.depth, self.sequence, self.rows, self.cols)  # początkowy root
        possible_solutions_for_node = {'ROOT', [root, root]}
        possible_solutions_for_depth = [{'ROOT', [root, root]}]

        # possible_solutions - dla kazdego node'a np {'L': [nowa_tablica, poprzednik] 'R': [nowa_tablica2, poprzednik]}
        # possible_solutions_for_depth - dla kazdej glebokosci np [[{'L': [nowa_tablica, poprzednik] 'R': [nowa_tablica2, poprzednik]}],
        # [{'U': [nowa_tablica3, poprzednik] 'D': [nowa_tablica4, poprzednik]}]]
        while True:
            possible_solutions = self.create_nodes_level(new_node)
            list_solutions.append(possible_solutions)

            for p in possible_solutions.values():
                if p == self.goal_board:
                    return possible_solutions.keys()  # tablica taka sama jak wzorcowa -> bierzemy ten zestaw 'L','R','L','U'...










