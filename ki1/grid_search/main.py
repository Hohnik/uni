from grid import Grid
from grid_gui import GridGUI


def main():
    width = 10
    height = 10

    state = Grid.create(width, height)
    grid = Grid(state)
    gui = GridGUI(grid)
    gui.mainloop()

if __name__ == "__main__": #guard
    main()