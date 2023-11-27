from grid import Grid


def test_grid_actions():
    grid = Grid(Grid.create())

    assert grid.actions(grid.initial) == ["RIGHT", "DOWN"]
    
    grid.initial[0][0] = 0
    grid.initial[9][9] = 1
    assert grid.actions(grid.initial) == ["UP", "LEFT"]

    grid.initial[9][9] = 0
    grid.initial[0][9] = 1
    assert grid.actions(grid.initial) == ["DOWN", "LEFT"]

    grid.initial[0][9] = 0
    grid.initial[9][0] = 1
    assert grid.actions(grid.initial) == ["UP", "RIGHT"]

    grid.initial[9][0] = 0
    grid.initial[0][5] = 1
    assert grid.actions(grid.initial) == ["RIGHT", "DOWN", "LEFT"]

    grid.initial[0][5] = 0
    grid.initial[5][0] = 1
    assert grid.actions(grid.initial) == ["UP", "RIGHT", "DOWN"]

def test_grid_actions_wall():
    grid = Grid(Grid.create(3,3))
    grid.initial[1][1] = -1

    grid.initial[0][0] = 0
    grid.initial[0][1] = 1
    assert grid.actions(grid.initial) == ["RIGHT", "LEFT"]

    grid.initial[0][1] = 0
    grid.initial[1][2] = 1
    assert grid.actions(grid.initial) == ["UP", "DOWN"]

    grid.initial[1][2] = 0
    grid.initial[2][1] = 1
    assert grid.actions(grid.initial) == ["RIGHT", "LEFT"]

    grid.initial[2][1] = 0
    grid.initial[1][0] = 1
    assert grid.actions(grid.initial) == ["UP", "DOWN"]

def test_find_player():
    grid = Grid(Grid.create())
    
    assert grid.find_player(grid.initial) == (0,0)

    grid.initial[0][0] = 0
    grid.initial[5][5] = 1
    assert grid.find_player(grid.initial) == (5,5)
    
    grid.initial[5][5] = 0
    grid.initial[9][9] = 1
    assert grid.find_player(grid.initial) == (9,9)

    grid.initial[9][9] = 0
    grid.initial[2][4] = 1
    assert grid.find_player(grid.initial) == (4,2)

def test_goal_test():
    grid = Grid(Grid.create(3,3))
    state = grid.initial
    path = ["DOWN","DOWN", "RIGHT", "RIGHT"]
    assertions = [False, False, False, True]

    for direction, assertion in zip(path, assertions):
        state = grid.result(state, direction)
        assert grid.goal_test(state) == assertion, f"{direction}, {assertion}"
        
