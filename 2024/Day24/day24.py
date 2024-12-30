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
    
  x, y = dict_to_bin(values, "x"), dict_to_bin(values, "y")
  target = str(bin(int(x,2) + int(y,2)))[2:]
  
  seen = set()
  variables = [var for _, var in temp_op]
  taken = [False] * (len(variables) + 1)
  def bt(e: int, n: int, parcial: list[str]) -> tuple:
    if n == 4:
      s_par = set(parcial)
      
      values = temp_vl.copy()
      operations = temp_op.copy()
      
      loops = 3
      while operations and loops:
        operation, result = operations.popleft()
        
        if result in s_par:
          index = get_index(parcial, result)
          n_result = parcial[index-1] if index % 2 == 1 else parcial[index+1]
        
        a, op, b = operation.split()
        
        if a not in values or b not in values:
          operations.append((operation, result))
          continue
      
        if result not in s_par:
          values[result] = do_operation(values[a], values[b], op)
        else:
          values[n_result] = do_operation(values[a], values[b], op)
        
        loops -= 1
      
      if not loops and operations:
        return []
      
      z = dict_to_bin(values, "z")
      return parcial if z == target else []
    
    for i, a in enumerate(variables[e:], start=e):
      if taken[i]:
        continue
      taken[i] = True
      for j, b in enumerate(variables[i+1:], start=i+1):
        if taken[j]:
          continue
        taken[j] = True
        
        # seen.add((a, b, n))
        # seen.add((b, a, n))
        
        if sol := bt(i+1, n+1, parcial + [a] + [b]):
          return sol
        
        taken[j] = False
      taken[i] = False
      
    return []
          
  
  return ",".join(sorted(bt(0, 0, [])))


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  # pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  # pr("Part Two:", part_two(read_file("./test3.in")))
  