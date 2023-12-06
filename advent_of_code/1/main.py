import re

counter = 0
result = 0

with open("data.txt", "r") as file:
    for line in file:
        digits = re.findall("\d", line)
        result += int(digits[0] + digits[-1])
        print(line, digits, result)


print(result)
