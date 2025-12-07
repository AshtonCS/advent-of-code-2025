from pathlib import Path
import math

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

invalid_sum = 0

for r in ranges:
    lb, ub = r.split('-')
    l_digits = len(lb)
    u_digits = len(ub)
    lower_bound = int(lb)
    upper_bound = int(ub)
    for i in range((l_digits + 1) // 2, u_digits // 2 + 1, 2):
        
        first_i = 0
        if(l_digits % 2 == 1):
            first_i = int(math.pow(10, i-1))
        else:
            first_i = lower_bound // int(math.pow(10, i))
        
        last_i = 0
        if(u_digits % 2 == 1):
            last_i = int(math.pow(10, i)) - 1
        else:
            last_i = upper_bound // int(math.pow(10, i))
        
        for j in range(first_i, last_i + 1):
            candidate = j * (int(math.pow(10, i)) + 1)
            if candidate >= lower_bound and candidate <= upper_bound:
                invalid_sum += candidate

print(invalid_sum)
        
        
