from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "input.txt"

moves = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            moves.append([-1 if line.strip()[0] == 'L' else 1, int(line.strip()[1:])])
except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

dial = 50
password = 0
leftZero = False
rightZero = False

for m in moves:
    if(leftZero and m[0] == 1):
        password += 1
    if(rightZero and m[0] == -1):
        password -= 1
    movement = (dial + m[0] * m[1])
    dial = movement % 100
    overflow = math.floor(movement / 100)
    password += abs(overflow)
    leftZero = dial == 0 and m[0] == -1
    rightZero = dial == 0 and m[0] == 1

if leftZero:
    password += 1

print(password)