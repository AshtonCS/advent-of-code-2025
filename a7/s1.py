from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "prac.txt"

diagram = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            diagram.append(line.replace('\n', ''))

except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

active_cols = [False] * len(diagram[0])
active_cols[diagram[0].find('S')] = True
counter = 0

for row in range(1, len(diagram)):
    for col in range(len(diagram[0])):
        if diagram[row][col] == '^' and active_cols[col]:
            if col != 0:
                active_cols[col-1] = True
            active_cols[col] = False
            if col != len(diagram[0]) - 1:
                active_cols[col+1] = True
            counter += 1

print(counter)

