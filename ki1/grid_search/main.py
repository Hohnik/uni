from grid import Grid
from grid_gui import GridGUI
from search import breadth_first_search


def main():
    width = 10
    height = 10

    initial = Grid.create(width, height)
    puzzle = Grid(initial=initial)
    #breadth_first_search(puzzle).solution()

    gui = GridGUI(puzzle, breadth_first_search)
    gui.mainloop()

if __name__ == "__main__": #guard
    main()