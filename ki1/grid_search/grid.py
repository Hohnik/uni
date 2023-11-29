class Grid(object):
    """
    The game state is a 2D list with 0's.
    The current position is represented by a 1
    A wall is represented by a -1
    """
    def __init__(self, initial):
        self.initial = initial
        self.goal = (len(initial[0])-1,len(initial)-1)

    @staticmethod
    def create(width=10, height=10):
        grid = [[0 for _ in range(width)] for _ in range(height)]
        grid[0][0] = 1
        return grid

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        player = self.find_player(state)

        if player[1] == 0 or state[player[1] -1][player[0]] == -1: # out of bounds || wall
            possible_actions.remove("UP")
       
        if player[1] == len(state) -1 or state[player[1] +1][player[0]] == -1: # out of bounds || wall
            possible_actions.remove("DOWN")

        if player[0] == len(state[0]) -1 or state[player[1]][player[0] +1] == -1: # out of bounds || wall
            possible_actions.remove("RIGHT")

        if player[0] == 0 or state[player[1]][player[0] -1] == -1: # out of bounds || wall
            possible_actions.remove("LEFT")
            
        return possible_actions
    

    def result(self, state:list[list], action: str):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        px, py = self.find_player(state)
        state[py][px] = 0

        match action:
            case "TOP":
                state[py -1][px] = 1
            case "RIGHT":
                state[py][px+1] = 1
            case "DOWN":
                state[py +1][px] = 1
            case "LEFT":
                state[py][px -1] = 1

        return state
        
    
    def goal_test(self, state):
        return self.find_player(state) == self.goal
    

    @staticmethod
    def find_player(state:list[list]):
        x, y = 0,0

        for j, row in enumerate(state): 
            if 1 not in row:
                continue
            for i, elem in enumerate(row):
                if elem == 1:
                    x = i
                    y = j

        return x,y
 

    def __str__(self):
        string = ""
        for row in self.initial:
            for elem in row:
                string += str(elem) + " "
            string += "\n"
        return string
