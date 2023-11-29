import puzzle

def test_puzzle_actions():
    puzzle = puzzle(puzzle.create())

    assert puzzle.actions(puzzle.initial) == ["RIGHT", "DOWN"]
    
    puzzle.initial[0][0] = 0
    puzzle.initial[9][9] = 1
    assert puzzle.actions(puzzle.initial) == ["UP", "LEFT"]

    puzzle.initial[9][9] = 0
    puzzle.initial[0][9] = 1
    assert puzzle.actions(puzzle.initial) == ["DOWN", "LEFT"]

    puzzle.initial[0][9] = 0
    puzzle.initial[9][0] = 1
    assert puzzle.actions(puzzle.initial) == ["UP", "RIGHT"]

    puzzle.initial[9][0] = 0
    puzzle.initial[0][5] = 1
    assert puzzle.actions(puzzle.initial) == ["RIGHT", "DOWN", "LEFT"]

    puzzle.initial[0][5] = 0
    puzzle.initial[5][0] = 1
    assert puzzle.actions(puzzle.initial) == ["UP", "RIGHT", "DOWN"]

def test_puzzle_actions_wall():
    puzzle = puzzle(puzzle.create(3,3))
    puzzle.initial[1][1] = -1

    puzzle.initial[0][0] = 0
    puzzle.initial[0][1] = 1
    assert puzzle.actions(puzzle.initial) == ["RIGHT", "LEFT"]

    puzzle.initial[0][1] = 0
    puzzle.initial[1][2] = 1
    assert puzzle.actions(puzzle.initial) == ["UP", "DOWN"]

    puzzle.initial[1][2] = 0
    puzzle.initial[2][1] = 1
    assert puzzle.actions(puzzle.initial) == ["RIGHT", "LEFT"]

    puzzle.initial[2][1] = 0
    puzzle.initial[1][0] = 1
    assert puzzle.actions(puzzle.initial) == ["UP", "DOWN"]

def test_find_player():
    puzzle = puzzle(puzzle.create())
    
    assert puzzle.find_player(puzzle.initial) == (0,0)

    puzzle.initial[0][0] = 0
    puzzle.initial[5][5] = 1
    assert puzzle.find_player(puzzle.initial) == (5,5)
    
    puzzle.initial[5][5] = 0
    puzzle.initial[9][9] = 1
    assert puzzle.find_player(puzzle.initial) == (9,9)

    puzzle.initial[9][9] = 0
    puzzle.initial[2][4] = 1
    assert puzzle.find_player(puzzle.initial) == (4,2)

def test_goal_test():
    puzzle = puzzle(puzzle.create(3,3))
    state = puzzle.initial
    path = ["DOWN","DOWN", "RIGHT", "RIGHT"]
    assertions = [False, False, False, True]

    for direction, assertion in zip(path, assertions):
        state = puzzle.result(state, direction)
        assert puzzle.goal_test(state) == assertion, f"{direction}, {assertion}"
        
