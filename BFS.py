from Node import Node
from functions import ZERO_POSITION, ROWS, COLS


class BFS:
    def __init__(self, LRUD_sequence, root_node):
        # self.starting_board = starting_board
        self.LRUD_sequence = LRUD_sequence
        self.root_node = root_node
        # self.goal_board = goal_board
        #
        # self.rows = rows
        # self.cols = cols
        # self.zero_loc = zero_loc


    def create_child_nodes(self, parent):
        child_nodes_parents = {}

        for s in self.strategy_parameter:           # ['L', 'R', 'U', 'D']
            child_nodes_parents[s] = parent.create_one_child(s, zero_location)

        return child_nodes_parents  # zwraca nam np zestaw {'L': [nowa_tablica, poprzednik] 'R': [nowa_tablica2, poprzednik]}

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








