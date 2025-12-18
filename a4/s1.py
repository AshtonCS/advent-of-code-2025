from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "input.txt"

grid = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            grid.append(list(line))
except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

def neighbourCount(r, c):
    counter = 0
    for y in range(r-1, r+2):
        if y >= 0 and y < len(grid):
            for x in range(c-1, c+2):
                if x >= 0 and x < len(grid[0])-1 and not (x == c and y == r) and grid[y][x] == '@':
                    counter += 1
    return counter

if __name__ == "__main__":
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])-1):
            if grid[row][col] == '@' and neighbourCount(row, col) < 4:
                total += 1
    print(total)