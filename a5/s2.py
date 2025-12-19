from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "input.txt"

ranges = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            vals = line.split('-')
            if len(vals) == 2:
                ranges.append([int(vals[0]), int(vals[1])])

except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

ranges = sorted(ranges, key=lambda x: x[0])
efficient_ranges = []

for range1 in ranges:
    range_added = False
    for range2 in efficient_ranges:
        if(range1[0] < range2[0] and range1[1] >= range2[0]):
            range2[0] = range1[0]
            range_added = True
        elif (range1[1] > range2[1] and range1[0] <= range2[1]):
            range2[1] = range1[1]
            range_added = True
        elif (range1[0] >= range2[0] and range1[1] <= range2[1]):
            range_added = True
    if not range_added:
        efficient_ranges.append(range1)

    print(efficient_ranges)

grand_total = 0
for range in efficient_ranges:
    grand_total += range[1] - range[0] + 1

print(grand_total)