from grid import Grid


def test_grid_actions():
    grid = Grid()

    assert grid.actions(grid.state) == ["RIGHT", "DOWN"]
    
    grid.state[0][0] = 0
    grid.state[9][9] = 1
    assert grid.actions(grid.state) == ["UP", "LEFT"]

    grid.state[9][9] = 0
    grid.state[0][9] = 1
    assert grid.actions(grid.state) == ["DOWN", "LEFT"]

    grid.state[0][9] = 0
    grid.state[9][0] = 1
    assert grid.actions(grid.state) == ["UP", "RIGHT"]

    grid.state[9][0] = 0
    grid.state[0][5] = 1
    assert grid.actions(grid.state) == ["RIGHT", "DOWN", "LEFT"]

    grid.state[0][5] = 0
    grid.state[5][0] = 1
    assert grid.actions(grid.state) == ["UP", "RIGHT", "DOWN"]

def test_grid_actions_wall():
    grid = Grid(3,3)
    grid.state[1][1] = -1

    grid.state[0][0] = 0
    grid.state[0][1] = 1
    assert grid.actions(grid.state) == ["RIGHT", "LEFT"]

    grid.state[0][1] = 0
    grid.state[1][2] = 1
    assert grid.actions(grid.state) == ["UP", "DOWN"]

    grid.state[1][2] = 0
    grid.state[2][1] = 1
    assert grid.actions(grid.state) == ["RIGHT", "LEFT"]

    grid.state[2][1] = 0
    grid.state[1][0] = 1
    assert grid.actions(grid.state) == ["UP", "DOWN"]

def test_find_player():
    grid = Grid()
    
    assert grid.find_player(grid.state) == (0,0)

    grid.state[0][0] = 0
    grid.state[5][5] = 1
    assert grid.find_player(grid.state) == (5,5)
    
    grid.state[5][5] = 0
    grid.state[9][9] = 1
    assert grid.find_player(grid.state) == (9,9)

