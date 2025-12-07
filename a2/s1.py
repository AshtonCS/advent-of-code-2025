from pathlib import Path

here = Path(__file__).parent
input_path = here / "input.txt"

try:
    with open(input_path, 'r') as file:
        first_line = file.readline()
        ranges = first_line.split(',');
except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(ranges)