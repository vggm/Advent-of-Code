from functools import reduce
import re

FILE = "./input.txt"

with open(FILE) as fr:
  worksheet = fr.read().strip().split("\n")

# split strings by spaces
worksheet = list(map(lambda x: re.split(r"\s+", x.strip()), worksheet))

# parse int the numbers (last row is the operation: + or *)
for i in range(len(worksheet) - 1):
  worksheet[i] = list(map(int, worksheet[i]))

# transform the matrix for better usage
worksheet = list(zip(*worksheet))
  

# =========== Part One =========== #

ans = 0
for op in worksheet:
  math_op = (lambda x, y: x*y) if op[-1] == "*" else (lambda x, y: x+y)
  ans += reduce(math_op, op[:-1])
    
print(f"Part One: {ans}")


# =========== Part Two =========== #

with open(FILE) as fr:
  worksheet = fr.read().strip().split("\n")

# remove the last line, only needs the op symbols
operations = re.split(r"\s+", worksheet.pop().strip())
lambda_operations = list(map(lambda op: (lambda x, y: x*y) if op == "*" else (lambda x, y: x+y), operations))

ans = 0
op_idx = 0

# depends on the symbol op it could be:
# - summation (neutral is 0) 
# - product notation (neutral is 1)
curr_sum = 0 if operations[0] == "+" else 1

for j in range(len(worksheet[0])):
  
  num = "" # it will store the num found during the iterations
  for i in range(len(worksheet)):
    if worksheet[i][j] != " ":
      num += worksheet[i][j]
  
  if not num: # num is empty, so its a separation column
    op_idx += 1 # inc index for the next op
    ans += curr_sum
    curr_sum = 0 if operations[op_idx] == "+" else 1 # reset
  
  else:
    # applies the operation and saves on the same variable
    # depends on the op symbol, but this line its like a (*= | +=) num
    curr_sum = lambda_operations[op_idx](int(num), curr_sum)

ans += curr_sum 

print(f"Part Two: {ans}")
