class Puzzle(object):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal 

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        current_position = self.find_current_position(state)

        if current_position < 10: # out of bounds || wall
            possible_actions.remove("UP")
        if current_position % 10 == 9: # out of bounds || wall
            possible_actions.remove("RIGHT")
        if current_position > 10*9-1: # out of bounds || wall
            possible_actions.remove("DOWN")
        if current_position % 10 == 0: # out of bounds || wall
            possible_actions.remove("LEFT")

        return possible_actions
    
    def result(self, state, action):
        current_position = self.find_current_position(state)
        next_state = state[:]

        delta = {"UP": -10, "RIGHT": 1, "DOWN": 10, "LEFT": -1}
        next_position = current_position + delta[action]
        next_state[current_position], next_state[next_position] =  next_state[next_position], next_state[current_position]

        return next_state

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal
    
    @staticmethod
    def find_current_position(state):
        return state.index(1)
    
class PuzzleGui(object):
    def __init__(self):
        self.root = Tk()
        self.state = [0 for x in range(10*10)]
        self.puzzle = EightPuzzle(tuple(self.state))
        self.solution = None
        self.b: List[Any] = [None] * 9
        self.init_gui()
        self.root.mainloop()