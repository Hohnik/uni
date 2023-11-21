import random
import time
from functools import partial
from tkinter import *
from typing import List, Any

from search import best_first_graph_search, breadth_first_search, astar_search, depth_limited_search


class EightPuzzle:
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal

    @staticmethod
    def is_solvable(state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    @staticmethod
    def find_blank_square(state):
        """Return the index of the blank square in a given state"""
        return state.index(0)


class EightPuzzleGui:

    def __init__(self):
        self.root = Tk()
        self.state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.puzzle = EightPuzzle(tuple(self.state))
        self.solution = None
        self.b: List[Any] = [None] * 9
        self.init_gui()
        self.root.mainloop()

    def init_gui(self):
        """Calls necessary functions"""
        self.scramble()
        self.create_buttons()
        self.create_static_buttons()

    def scramble(self):
        """Scrambles the puzzle starting from the goal state"""

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        scramble = []
        for _ in range(60):
            scramble.append(random.choice(possible_actions))

        for move in scramble:
            if move in self.puzzle.actions(self.state):
                self.state = list(self.puzzle.result(self.state, move))
                self.puzzle = EightPuzzle(tuple(self.state))
                self.create_buttons()

    def create_buttons(self):
        """Creates dynamic buttons"""

        self.b[0] = Button(self.root, text=f'{self.state[0]}' if self.state[0] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'),
                           command=partial(self.exchange, 0))
        self.b[0].grid(row=0, column=0, ipady=40)
        self.b[1] = Button(self.root, text=f'{self.state[1]}' if self.state[1] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 1))
        self.b[1].grid(row=0, column=1, ipady=40)
        self.b[2] = Button(self.root, text=f'{self.state[2]}' if self.state[2] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 2))
        self.b[2].grid(row=0, column=2, ipady=40)
        self.b[3] = Button(self.root, text=f'{self.state[3]}' if self.state[3] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 3))
        self.b[3].grid(row=1, column=0, ipady=40)
        self.b[4] = Button(self.root, text=f'{self.state[4]}' if self.state[4] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 4))
        self.b[4].grid(row=1, column=1, ipady=40)
        self.b[5] = Button(self.root, text=f'{self.state[5]}' if self.state[5] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 5))
        self.b[5].grid(row=1, column=2, ipady=40)
        self.b[6] = Button(self.root, text=f'{self.state[6]}' if self.state[6] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 6))
        self.b[6].grid(row=2, column=0, ipady=40)
        self.b[7] = Button(self.root, text=f'{self.state[7]}' if self.state[7] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 7))
        self.b[7].grid(row=2, column=1, ipady=40)
        self.b[8] = Button(self.root, text=f'{self.state[8]}' if self.state[8] != 0 else None, width=6,
                           font=('Helvetica', 40, 'bold'), command=partial(self.exchange, 8))
        self.b[8].grid(row=2, column=2, ipady=40)

    def create_static_buttons(self):
        """Creates scramble and solve buttons"""

        scramble_btn = Button(self.root, text='Scramble', font=('Helvetica', 30, 'bold'), width=8,
                              command=partial(self.init_gui))
        scramble_btn.grid(row=3, column=0, ipady=10)
        solve_btn = Button(self.root, text='Solve', font=('Helvetica', 30, 'bold'), width=8,
                           command=partial(self.solve_steps))
        solve_btn.grid(row=3, column=2, ipady=10)

    def exchange(self, index):
        """Interchanges the position of the selected tile with the zero tile under certain conditions"""

        zero_ix = list(self.state).index(0)
        actions = self.puzzle.actions(self.state)
        current_action = ''
        i_diff = index // 3 - zero_ix // 3
        j_diff = index % 3 - zero_ix % 3
        if i_diff == 1:
            current_action += 'DOWN'
        elif i_diff == -1:
            current_action += 'UP'

        if j_diff == 1:
            current_action += 'RIGHT'
        elif j_diff == -1:
            current_action += 'LEFT'

        if abs(i_diff) + abs(j_diff) != 1:
            current_action = ''

        if current_action in actions:
            self.b[zero_ix].grid_forget()
            self.b[zero_ix] = Button(self.root, text=f'{self.state[index]}', width=6, font=('Helvetica', 40, 'bold'),
                                     command=partial(self.exchange, zero_ix))
            self.b[zero_ix].grid(row=zero_ix // 3, column=zero_ix % 3, ipady=40)
            self.b[index].grid_forget()
            self.b[index] = Button(self.root, text=None, width=6, font=('Helvetica', 40, 'bold'),
                                   command=partial(self.exchange, index))
            self.b[index].grid(row=index // 3, column=index % 3, ipady=40)
            self.state[zero_ix], self.state[index] = self.state[index], self.state[zero_ix]
            self.puzzle = EightPuzzle(tuple(self.state))

    def solve_steps(self):
        """Solves the puzzle step by step"""

        self.solution = self.solve()
        print(self.solution)

        for move in self.solution:
            self.state = self.puzzle.result(self.state, move)
            self.create_buttons()
            self.root.update()
            self.root.after(0, time.sleep(0.1))

    def solve(self):
        """Solves the puzzle using your solution. Needs to return a sequence of actions (as list)
         to go from initial state to goal state."""
        if self.puzzle.is_solvable(self.state):
            #return breadth_first_search(self.puzzle).solution()
            #return best_first_graph_search(self.puzzle, lambda node:node.path_cost).solution()
            #return depth_limited_search(self.puzzle, 20).solution()
            return astar_search(self.puzzle).solution()
        else:
            return "Puzzle non-solvable"


if __name__ == "__main__":
    EightPuzzleGui()
