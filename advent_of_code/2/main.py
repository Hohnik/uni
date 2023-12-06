import re


def is_under(number, count):
    if number < count:
        return True
    return False


def stones_ok(dct):
    if is_under(12, dct["red"]):
        return False
    if is_under(13, dct["green"]):
        return False
    if is_under(14, dct["blue"]):
        return False
    return True


result = 0


with open("data.txt", "r") as file:
    for line in file:
        stones = {"red": 0, "green": 0, "blue": 0}
        game_id, game = line.strip().split(":")  # 3 blue, 6 red; 4 red, 3 green; 4 green, 16 red; 14 blue, 1 green
        game_id = int(game_id.split()[1])
        good_draws = True
        for draws in game.strip().split(";"):  # 2 blue, 1 red, 9 green;
            for draw in draws.strip().split(","):  # 10 green,
                number, color = draw.split()
                stones[color] = int(number)

            if not stones_ok(stones):
                good_draws = False

        if good_draws:
            result += game_id

        # print(f"Game {game_id}: ", game, "\n", good_draws)

print(result)
