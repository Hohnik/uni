from functools import partial
from tkinter import Button, Tk


class Puzzle(object):
    def __init__(self, initial, goal = [1 if x == 99 else 0 for x in range(10*10)]):
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
        self.state = [1 if x == 0 else 0 for x in range(10*10)]
        self.puzzle = Puzzle(self.state)
        self.solution = None
        self.buttons = [None] * (10*10)
        self.init_gui()
        self.root.mainloop()

    def init_gui(self):
        self.create_buttons()
        self.create_static_buttons()

    def create_buttons(self):
        for i, _ in enumerate(self.buttons):
            self.buttons[i] = Button(self.root,
                                     text=f'P' if self.state[i] == 1 else None, 
                                     width=2,
                                     height=1,
                                     fg="cornflowerblue",
                                     bg="gray20",
                                     font=('Helvetica', 40, 'bold'),
                                     command=lambda: print("Hi!"))
            self.buttons[i].grid(row=i//10, column=i%10, ipady=10)
            print(f"Created Button {i}")

    def create_static_buttons(self):
        solve_btn = Button(self.root, text='Solve', font=('Helvetica', 30, 'bold'), width=8,
                           command=partial(self.solve_steps))
        solve_btn.grid(row=10, column=3, ipady=10, columnspan=4)

    def solve_steps(self):
        pass
    
    def exchange(self, index):
        pass



if __name__ == "__main__":
    PuzzleGui()