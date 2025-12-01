from pathlib import Path

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
password = 0;

for m in moves:
    dial = (dial + m[0] * m[1]) % 100
    if dial == 0:
        password += 1

print(password)