import string


def main():
    schematic = extractFile("data.txt")
    result = 0
    [print(i, x) for i, x in enumerate(schematic)]
    for i, row1, row2, row3 in zip(range(len(schematic)), schematic, schematic[1:], schematic[2:]):
        if i == 0:
            number = find_numbers(
                ["." for _ in range(len(row1))],
                row1,
                row2,
            )
            print("i == 0: ", number)
            result += number
            continue

        if i == len(schematic) - 3:
            number = find_numbers(
                row2,
                row3,
                ["." for _ in range(len(row1))],
            )
            print("i ==-1: ", number)
            result += number
            continue

        number = find_numbers(
            row1,
            row2,
            row3,
        )
        print(f"i == {i}: ", number)
        result += number

    print(result)


def find_numbers(row1, row2, row3):
    total_number = 0
    is_surrounded = False
    number_constructor = ""

    for i, char in enumerate(row2):
        number_constructor += char if is_digit(char) else ""

        if is_digit(char) and not is_surrounded:
            is_surrounded = check_surroundings(i, row1, row2, row3)

        if not is_digit(char) and is_surrounded:
            total_number += int(number_constructor)

        if not is_digit(char):
            number_constructor = ""
            is_surrounded = False

    return total_number


def extractFile(path):
    schematic = []
    with open(path, "r") as file:
        for line in file:
            schematic.append(line.strip())
    return schematic


def is_digit(character):
    return True if character in string.digits else False


def check_surroundings(i, lst1, lst2, lst3):
    purged_punctuation = "".join(string.punctuation.split("."))

    surroundings = [
        lst1[i],
        lst3[i],
    ]
    if i > 0:
        surroundings += [
            lst1[i - 1],
            lst2[i - 1],
            lst3[i - 1],
        ]
    if i < len(surroundings):
        surroundings += [
            lst1[i + 1],
            lst2[i + 1],
            lst3[i + 1],
        ]
    for elem in surroundings:
        if elem in purged_punctuation:
            return True
    return False


if __name__ == "__main__":
    main()
