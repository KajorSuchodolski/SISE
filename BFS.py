from Node import Node


class BFS:
    def __init__(self, starting_board, strategy_parameter, goal_board, rows, cols, zero_loc):
        self.starting_board = starting_board
        self.strategy_parameter = strategy_parameter
        self.goal_board = goal_board

        self.rows = rows
        self.cols = cols
        self.zero_loc = zero_loc

    def create_child_nodes(self, parent):     # tworzenie
        possible_solutions = {}

        for s in self.strategy_parameter:           # ['L', 'R', 'U', 'D']
            status = parent.move(s, self.zero_loc)[1]
            if status:
                possible_solutions[s] = [parent.move(s, self.zero_loc)[0], parent]

        return possible_solutions  # zwraca nam np zestaw {'L': [nowa_tablica, poprzednik] 'R': [nowa_tablica2, poprzednik]}

    def bfs_algorithm(self):
        root = Node(self.starting_board, self.parent_node, self.depth, self.sequence, self.rows, self.cols)  # początkowy root
        possible_solutions_for_node = {'ROOT', [root, root]}
        possible_solutions_for_depth = [{'ROOT', [root, root]}]

        # possible_solutions - dla kazdego node'a np {'L': [nowa_tablica, poprzednik] 'R': [nowa_tablica2, poprzednik]}
        # possible_solutions_for_depth - dla kazdej glebokosci np [[{'L': [nowa_tablica, poprzednik] 'R': [nowa_tablica2, poprzednik]}],
        # [{'U': [nowa_tablica3, poprzednik] 'D': [nowa_tablica4, poprzednik]}]]
        while True:
            for p_depth in possible_solutions_for_depth:
                for p in possible_solutions_for_node:            # dla każdego roota odchodzacego od roota
                    possible_solutions_for_node = self.create_child_nodes(p)
                    if self.goal_board in possible_solutions_for_node.values()[0]:
                        print("Solution found")
                        break
                    possible_solutions_for_depth.append(possible_solutions_for_node)








