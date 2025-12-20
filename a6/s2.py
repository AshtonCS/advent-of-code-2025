# Note: This is an incorrect solution
# After consulting others' solutions, I realised my problem
# was that by splitting so early on, I could not accurately tell
# which digits belonged to which numbers. To fix my program, I would
# save each line of the input file to a string, then iterate by index,
# then iterate backward through it. I would store the list of numbers
# until I saw a column with an operator in the final index, then I would
# apply that operator onto the list, add to the total and clear the list
# for the next operations.


from pathlib import Path
import math

here = Path(__file__).parent
input_path = here / "prac.txt"

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
        split_nums[i][:len(digits)] = digits
    
    print(split_nums)

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

