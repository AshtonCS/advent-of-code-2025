from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "input.txt"

problems = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            problems.append(line.split())

except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

total = 0

print(total)

for p in range(len(problems[0])):
    calc = problems[0][p]
    for num in range(1, len(problems) - 2):
        if(problems[len(problems[0])-1][p] == '+'):
            calc = calc + problems[num][p]
        else:
            calc = calc * problems[num][p]
        


