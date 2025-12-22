from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "input.txt"

diagram = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            diagram.append(line.replace('\n', ''))

except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(diagram)
