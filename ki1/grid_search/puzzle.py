from functools import partial
from random import random
from tkinter import Button, Tk

from search import astar_search, breadth_first_search, best_first_graph_search, depth_limited_search

initial_state =(
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0,-1,-1,-1,-1,-1, 0, 0, 0, 
    0,-1, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0,-1, 1, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
)
initial_goal = 33

class Puzzle(object):
    def __init__(self, initial, goal= 99 ): # numbers over 91 take over 10 sec
        self.initial = initial
        self.goal = goal 
        self.generate_wall()

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        current_position = self.find_current_position(state)

        if current_position < 10 or state[current_position -10] == -1:
            possible_actions.remove("UP")
        if current_position % 10 == 9 or state[current_position +1] == -1:
            possible_actions.remove("RIGHT")
        if current_position > 10*9-1 or state[current_position +10] == -1:
            possible_actions.remove("DOWN")
        if current_position % 10 == 0 or state[current_position -1] == -1:
            possible_actions.remove("LEFT")

        return possible_actions
    
    def result(self, state, action):
        current_position = self.find_current_position(state)
        next_state = list(state)[:]

        delta = {"UP": -10, "RIGHT": 1, "DOWN": 10, "LEFT": -1}
        next_position = current_position + delta[action]
        next_state[current_position] = 2
        next_state[next_position] = 1

        return tuple(next_state)

    def generate_wall(self):
        print(random())
        
        
    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state.index(1) == self.goal
        #return state == self.goal
    
    @staticmethod
    def find_current_position(state):
        return state.index(1)

class PuzzleGui(object):
    def __init__(self):
        self.root = Tk()
        self.state = initial_state#tuple([1 if x == 0 else 0 for x in range(10*10)])
        self.puzzle = Puzzle(initial_state, initial_goal)#Puzzle(self.state)
        self.solution = None
        self.buttons: list[Button] = [None] * (10*10)
        self.init_gui()
        self.root.mainloop()

    def init_gui(self):
        self.create_buttons()
        self.create_static_buttons()

    def create_buttons(self):
        for i, _ in enumerate(self.buttons):
            def getTextBy(number):
                if number == 1:
                    return "P"
                if number == 2:
                    return "+"
                if number == -1:
                    return "#"
                return None

            self.buttons[i] = Button(self.root,
                                     text=getTextBy(self.state[i]), 
                                     width=2,
                                     height=1,
                                     fg="cornflowerblue",
                                     bg="gray20",
                                     font=('Helvetica', 40, 'bold'),
                                     command=partial(self.add_wall, i))
            
            self.buttons[i].grid(row=i//10, column=i%10, ipady=10)

    def create_static_buttons(self):
        solve_btn = Button(self.root, text='Solve', font=('Helvetica', 30, 'bold'), width=8,
                           command=partial(self.solve_steps))
        solve_btn.grid(row=10, column=3, ipady=10, columnspan=4)
    
    def add_wall(self, index):
        self.buttons[index].configure(text="#")

        self.state = list(self.state)
        self.state[index] = -1
        self.state = tuple(self.state)

        self.puzzle = Puzzle(self.state)

    def exchange(self, index):
        player_index = self.state.index(1)
        actions = self.puzzle.actions(self.state)
        current_action = ""

        row_diff = index // 10 - player_index // 10
        col_diff = index % 10 - player_index % 10

        if row_diff == 1:
            current_action = "DOWN"
        elif row_diff == -1:
            current_action = "UP"

        if col_diff == 1:
            current_action = "RIGHT"
        elif col_diff == -1:
            current_action = "LEFT"
            
        if abs(row_diff) + abs(col_diff) != 1:
            current_action = ""

        if current_action in actions:
            self.buttons[player_index].configure(text="o")
            self.buttons[index].configure(text="P")

            self.state = list(self.state)
            self.state[player_index] = 2
            self.state[index] = 1
            self.state = tuple(self.state)

            self.puzzle = Puzzle(self.state)

    def solve_steps(self):
        self.solution = self.solve()
        print(self.solution)

        for move in self.solution:
            self.state = self.puzzle.result(self.state, move)
            self.create_buttons()
            self.root.update()
            #self.root.after(0, time.sleep(0.1))

    def solve(self):
        #* the search algorithms return a Node object.
        #* The Node object holds a list of the taken actions.
        return breadth_first_search(self.puzzle).solution()
        #return best_first_graph_search(self.puzzle, lambda node:node.path_cost).solution()
        #return depth_limited_search(self.puzzle, 20).solution()
        #return astar_search(self.puzzle).solution()



if __name__ == "__main__":
    PuzzleGui()