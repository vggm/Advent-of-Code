from collections import deque
from functools import cache
import pyperclip as cp
import sys


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip()


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 
 
def get_params(file_input: str) -> tuple[dict[str, bool], deque[tuple[str, str]]]:
  values, operations = file_input.split("\n\n")
  
  values: dict[str, bool] = {var: val == "1" for var, val  in  map(lambda x: x.split(": "), values.split("\n"))}
  operations: list[tuple[str, str]] = list(map(lambda x: x.split(" -> "), operations.split("\n")))
    
  return values, deque(operations)
 
 
def do_operation(a: bool, b: bool, op: str) -> bool:
  res = -1
  if op == "AND":
    res = a and b
  
  elif op == "OR":
    res = a or b
  
  elif op == "XOR":
    res = a ^ b
  
  return res


def dict_to_bin(nums_dict: dict[str, bool], num: str) -> str:
  num_values = {k: v for k, v in nums_dict.items() if k[0] == num}
  
  res = []
  for k in sorted(num_values, reverse=True):
    res.append("1" if num_values[k] else "0")
  
  return "".join(res)


def get_index(l: list[str], t: str) -> int:
  for i, val in enumerate(l):
    if val == t:
      return i
  
  return -1


def part_one(file_input: str) -> int:
  values, operations = get_params(file_input)
  
  while operations:
    operation, result = operations.popleft()
    a, op, b = operation.split()
    
    if a not in values or b not in values:
      operations.append((operation, result))
      continue
    
    values[result] = do_operation(values[a], values[b], op)

  return int(dict_to_bin(values, "z"), 2)


def part_two(file_input: list[str]) -> int:
  values, operations = get_params(file_input)
  
  temp_vl = values.copy()
  temp_op = operations.copy()
  
  while operations:
    operation, result = operations.popleft()
    a, op, b = operation.split()
    
    if a not in values or b not in values:
      operations.append((operation, result))
      continue
    
    values[result] = do_operation(values[a], values[b], op)
    
  x, y, z = dict_to_bin(values, "x"), dict_to_bin(values, "y"), dict_to_bin(values, "z")
  target = str(bin(int(x,2) + int(y,2)))[2:]
  
  print(f"X: {x}")
  print(f"Y: {y}")
  print(f"Z: {z}")
  print(f"T: {target}")
  
  cnt = 0
  for i, j in zip(z, target):
    if i != j:
      cnt += 1
  
  return cnt // 2


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  # pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  # pr("Part Two:", part_two(read_file("./test3.in")))
  