from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "prac.txt"

grid = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            grid.append(list(line))
except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(grid)