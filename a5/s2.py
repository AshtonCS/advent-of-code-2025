from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "prac.txt"

quality = []
available = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            vals = line.split('-')
            if len(vals) == 2:
                quality.append([int(vals[0]), int(vals[1])])
            elif line != "\n":
                available.append(int(line))

except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(quality, available)