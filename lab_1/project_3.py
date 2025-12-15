import re

lines = []

while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

for line in lines:
    numbers = re.findall(r'\d+', line)
    if numbers:
        print(", ".join(numbers))
