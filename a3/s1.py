from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "input.txt"

joltages = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            joltages.append(str(line).strip("\n"))
except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

def maxSubstring(bank, length):
    maxIdx = 0
    for i in range(0, len(bank) - length):
        if int(bank[i]) > int(bank[maxIdx]):
            maxIdx = i
    print(bank, length)
    return int(bank[maxIdx]) * math.pow(10, length-1) + maxSubstring(bank[maxIdx+1:], length - 1)

if __name__ == "__main__":
    total = 0
    for bank in joltages:
        total += maxSubstring(bank, 2)
    print(total)

