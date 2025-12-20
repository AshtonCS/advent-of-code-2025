from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "input.txt"

problems = []

try:
    with open(input_path, 'r') as file:
        for line in file:
            problems.append(line.split())

except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

total = 0

for p in range(len(problems[0])):
    sign = problems[len(problems)-1][p]
    split_nums = [[' ' for _ in range(4)] for _ in range(len(problems) - 1)]

    for i in range(len(problems) - 1):
        digits = list(problems[i][p])
        if(sign == '*'):
            digits.reverse()
        split_nums[i][:len(digits)] = digits

    ceph_nums = ["" for _ in range(4)]
    for num in split_nums:
        for digit in range(len(num)):
            if digit != ' ':
                ceph_nums[digit] += num[digit]

    subtotal = 0
    if(sign == '*'):
        subtotal = 1
    
    for num in ceph_nums:
        if len(num.split()) != 0:
            if sign == '+':
                subtotal += int(num)
            else:
                subtotal *= int(num)
        
    print("Numbers: ", ceph_nums, ", Subtotal: ", subtotal, ", Operator: ", sign)
    total += subtotal

print(total)

