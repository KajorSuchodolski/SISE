from Node import Node
from functions import get_position
import datetime


class Astar:
    def __init__(self, starting_board, goal_board, method):
        self.starting_board = starting_board
        self.goal_board = goal_board
        self.method = method

    def heuristic_distance(self, node):
        score = 0
        size = len(node.board) * len(node.board[0])

        if self.method == 'manh':
            for value in range(size - 1):
                current_row, current_column = get_position(value, node.board)
                goal_row, goal_column = get_position(value, self.goal_board)
                if abs(goal_row - current_row) + abs(goal_column - current_column) != 0:
                    score += abs(goal_row - current_row) + abs(goal_column - current_column)
            return score
        else:
            for value in range(size - 1):
                current_row, current_column = get_position(value, node.board)
                goal_row, goal_column = get_position(value, self.goal_board)
                if abs(goal_row - current_row) + abs(goal_column - current_column) != 0:
                    score += 1
            return score

    def a_star(self):
        directions = ['L', 'R', 'U', 'D']
        LRUD_solution_sequence = []
        parents_queue = []
        children_queue = []
        visited_boards = []
        one_or_more_distances = []
        solution_length = 0


        depth = 0
        processed_nodes_stats = 0

        start_time = datetime.datetime.now()
        root = Node(self.starting_board, None, None)
        visited_nodes_stats = 1


        if root.board == self.goal_board:
            end_time = datetime.datetime.now()
            exec_time = (end_time - start_time).total_seconds() * 1000

            LRUD_solution_sequence = None
            solution_length = 0

            print('Solution found')

            return LRUD_solution_sequence, solution_length, depth, exec_time, visited_nodes_stats, processed_nodes_stats

        else:
            parents_queue.append([root, 'root node'])
            shortest_distance = self.heuristic_distance(root)
            visited_boards.append(root.board)
            processed_nodes_stats += 1

        while parents_queue:
            depth += 1
            children_queue.clear()

            for parent in parents_queue:
                for direction in directions:
                    child = parent[0].create_one_child(direction)
                    if child is not None:
                        child_distance = self.heuristic_distance(child)

                        if child.board in visited_boards:
                            visited_nodes_stats += 1

                        else:
                            children_queue.append([child, child_distance])
                            visited_boards.append(child.board)

                            processed_nodes_stats += 1
                            visited_nodes_stats += 1

            parents_queue.clear()

            if len(children_queue) >= 1:
                minimum_child_distance = children_queue[0][1]

                for child in children_queue:
                    if child[1] < minimum_child_distance:
                        minimum_child_distance = child[1]

                for child in children_queue:
                    if child[1] == minimum_child_distance:
                        one_or_more_distances.append(child)

                if minimum_child_distance != 0:
                    if len(one_or_more_distances) > 1:
                        for same_distance_child in one_or_more_distances:
                            parents_queue.append(same_distance_child)
                    else:
                        parents_queue.append(one_or_more_distances[0])


                else:
                    end_time = datetime.datetime.now()
                    exec_time = (end_time - start_time).total_seconds() * 1000

                    for node in one_or_more_distances:
                        if node[1] == minimum_child_distance:
                            node_goal = node[0]

                    while node_goal:
                        if node_goal.direction is not None:
                            LRUD_solution_sequence.append(node_goal.direction)
                            print(node_goal.direction)
                        node_goal = node_goal.parent_node

                    LRUD_solution_sequence.reverse()

                    solution_length = len(LRUD_solution_sequence)

                    print('Solution found')

                    print(LRUD_solution_sequence)
                    print(depth)
                    print(exec_time)
                    print(visited_nodes_stats)
                    print(processed_nodes_stats)

                    return LRUD_solution_sequence, solution_length, depth, exec_time, \
                           visited_nodes_stats, processed_nodes_stats

        end_time = datetime.datetime.now()
        exec_time = (end_time - start_time).total_seconds() * 1000

        solution_length = -1
        LRUD_solution_sequence = None

        print('Solution not found')

        return LRUD_solution_sequence, solution_length, depth, exec_time, visited_nodes_stats, processed_nodes_stats
