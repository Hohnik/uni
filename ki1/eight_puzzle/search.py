from collections import deque
from utils import PriorityQueue, Node


def breadth_first_search(puzzle):
    node = Node(puzzle.initial)
    if puzzle.goal_test(node.state):
        return node
    frontier = deque([node])
    reached = []
    # counter = 0
    
    while not is_empty(frontier):
        node = frontier.popleft()
        # if counter > 10_000:
        #     return False
        
        for child in node.expand(puzzle):
            s = child.state
            # counter += 1
            
            if puzzle.goal_test(s):
                return child
            
            if s not in reached:
                reached.append(s)
                frontier.append(child)

    return False

def depth_limited_search(puzzle, limit): #TODO Fix!

    node = Node(puzzle.initial)
    frontier = deque(node) # FIFO (Stack)
    reached = deque()
    result = None

    while frontier:
        node = frontier.pop()

        if puzzle.goal_test(node.state):
            return node.solution()

        if node.depth >= limit:
            continue
        if node.state not in reached:
            for child in node.expand(puzzle):
                frontier.append(child)
                reached.append(child.state)

    return result

def best_first_graph_search(puzzle, f):
    """Search the nodes with the lowest f scores first."""
    node = Node(puzzle.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    reached = dict()
    # poped_counter = 0 
    # child_counter = 0 

    while not is_empty(frontier):
        node = frontier.pop()

        # print(f"\nNode {poped_counter} cost: ", f(node))
        # poped_counter += 1

        if puzzle.goal_test(node.state):
            return node
        
        for child in node.expand(puzzle):
            # print(f"Node {child_counter} cost: ", f(child))
            # child_counter += 1

            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.append(child)

    return False

def h(node):
    """Default heuristic function h(n) = number of misplaced tiles """
    mannhattan_distance = [
        (4, 3, 2, 3, 2, 1, 2, 1, 0), # 0
        (0, 1, 2, 1, 2, 3, 2, 3, 4), # 1
        (1, 0, 1, 2, 1, 2, 3, 2, 3), # 2
        (2, 1, 0, 3, 2, 1, 4, 3, 2), # 3 
        (1, 2, 3, 0, 1, 2, 1, 2, 3), # 4
        (2, 1, 2, 1, 0, 1, 2, 1, 2), # 5
        (3, 2, 1, 2, 1, 0, 3, 2, 1), # 6
        (2, 3, 4, 1, 2, 3, 0, 1, 2), # 7
        (3, 2, 3, 2, 1, 2, 1, 0, 1), # 8
        ]

    h_cost = 0
    
    for position, digit in enumerate(node.state):
       digit_cost = mannhattan_distance[digit][position]
       h_cost += digit_cost
       
    return h_cost

def g(node):
    return node.path_cost

def f(node):
    return g(node) + h(node)

def astar_search(puzzle):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the f function when you call astar_search."""
    return best_first_graph_search(puzzle, f)

def is_empty(frontier):
    return True if len(frontier) == 0 else False
