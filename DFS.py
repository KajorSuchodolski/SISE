import time

from Node import Node


class DFS:
    def __init__(self, starting_board, goal_board, lrud_sequence):
        self.lrud_sequence = lrud_sequence
        self.starting_board = starting_board
        self.goal_board = goal_board
        self.max_depth: int = 15
        self.max_depth_visited: int = 0
        self.visited = []
        self.done: [[]] = None

        self.processed: int = 0
        self.visits: int = 0
        self.time: float = 0.0

    def dfs(self):

        print("umu")

        # global max_frontier_size, goal_node, max_search_depth
        #
        # explored, stack = set(), list([Node(self.starting_board, 'Root Node', None)])
        #
        # while stack:
        #
        #     node = stack.pop()
        #
        #     explored.add(node.direction)
        #
        #     if node.board == self.goal_board:
        #         goal_node = node
        #         return stack
        #
        #     neighbors = reversed(expand(node))
        #
        #     for neighbor in neighbors:
        #         if neighbor.map not in explored:
        #             stack.append(neighbor)
        #             explored.add(neighbor.map)
        #
        #             if neighbor.depth > max_search_depth:
        #                 max_search_depth += 1
        #
        #     if len(stack) > max_frontier_size:
        #         max_frontier_size = len(stack)

        # start_time = time.time()
        # current_node = Node(self.starting_board, 'Root Node', None)
        # self.find_solution(current_node, 0)
        # self.time = (time.time() - start_time) * 1000
        # self.visited.reverse()


    # def find_solution(self, node, depth):
    #
    #     if self.done is not None:
    #         print(self.done)
    #         return
    #
    #     # if depth > self.max_depth_visited:
    #     #     self.max_depth_visited = depth
    #
    #     if node.board == self.goal_board:
    #         self.done = node.board
    #         return
    #
    #     if depth > self.max_depth:
    #         return
    #
    #     self.visits += 1
    #     self.processed += 1
    #
    #     directions = []
    #     # w celu gorszego dzialania zakkomentowac
    #     # node.remove_moves_two()
    #     for direction in self.lrud_sequence:
    #         if node.move(direction, True):
    #             directions.append(direction)
    #
    #     for direction in directions:
    #         node = node.create_one_child(direction)
    #         self.find_solution(node, depth + 1)
    #
    #         if self.done is not None:
    #             # while node:
    #             #     if node.direction is not None:
    #             #         self.visited.append(node.direction)
    #             #     node = node.parent_node
    #             print(self.done)
    #             self.visited.append(node.direction)
    #             return
    #     return
