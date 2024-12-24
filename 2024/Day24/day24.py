from collections import deque
import sys
import pyperclip as cp


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


def part_one(file_input: str) -> int:
  values, operations = get_params(file_input)
  
  max_z = 0
  while operations:
    operation, result = operations.popleft()
    a, op, b = operation.split()
    if a not in values or b not in values:
      operations.append((operation, result))
      continue
    
    if result[0] == "z":
      max_z = max(max_z, int(result[1:]))
    
    values[result] = do_operation(values[a], values[b], op)
    
  res = [""] * (max_z + 1)
  for k, v in values.items():
    if k[0] == "z":
      index = max_z - int(k[1:])
      res[index] = "1" if v else "0"

  return int("".join(res), 2)


def part_two(file_input: list[str]) -> int:
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  # pr("Part Two:", part_two(file_input))
  