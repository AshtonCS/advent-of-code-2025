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
solutions = []

for r in ranges:
    lb, ub = r.split('-')
    l_digits = len(lb)
    u_digits = len(ub)
    lower_bound = int(lb)
    upper_bound = int(ub)
    for i in range(l_digits, u_digits + 1): # i is the number of digits in the candidate number
        for j in range(1, i): # j is the length of the substring being considered (only in sizes that are multiples of i)
            if i % j != 0:
                continue
            first_i = 0
            if(l_digits % i != 0): # first_i is the minimum value with j digits if the lower bound has less than i digits
                first_i = int(math.pow(10, j-1))
            else:
                first_i = lower_bound // int(math.pow(10, (i-j))) # Otherwise, it's the first j numbers of lower bound
            
            last_i = 0
            if(u_digits % i != 0): # last_i is the maximum value with j digits if the upper bound has more than i digits
                last_i = int(math.pow(10, j)) - 1
            else:
                last_i = upper_bound // int(math.pow(10, i-j)) # Otherwise, it's the first j numbers of upper bound
            
            for k in range(first_i, last_i + 1):
                candidate = 0
                for l in range(0, int(i/j)):
                    candidate += k * int(math.pow(10, l * j))
                if candidate >= lower_bound and candidate <= upper_bound and candidate not in solutions:
                    invalid_sum += candidate
                    solutions.append(candidate)

print(invalid_sum)
        
        
