from Node import Node


class DFS:
    def __init__(self, starting_board, goal_board, LRUD_sequence):
        self.LRUD_sequence = LRUD_sequence
        self.starting_board = starting_board
        self.goal_board = goal_board
        self.max_depth = 20

    def dfs(self):
        current_node = Node(self.goal_board, 'Root Node', None, self.LRUD_sequence, no)
        depth = 0
        goal = []
        visited_nodes = 1

        while True:
            direction = current_node.LRUD_sequence[0]
            if self.starting_board == current_node.board:
                return "Hurrra kurwa wygrales wycieczke do tadzykistanu", goal, depth

            elif depth >= self.max_depth:
                current_node = current_node.parent_node
                depth -= 1
                goal.pop(len(goal) - 1)

            elif len(current_node.LRUD_sequence) != 0:
                node_tmp = current_node.create_one_child(direction)

                if node_tmp is not None:
                    current_node = node_tmp
                    depth += 1
                    goal.append(direction)

                else:
                    current_node.pop_LRUD_element()

            else:
                current_node = current_node.parent_node
                depth -= 1



