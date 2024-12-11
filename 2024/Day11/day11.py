import sys
import pyperclip as cp
from functools import cache


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split(" ")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

@cache
def apply_rules_recursive(stone: str, iteration: int) -> int:
  if iteration == 0: # base case
    return 1
  
  if stone == "0": # 0 -> 1
    return apply_rules_recursive("1", iteration - 1) 
  
  if len(stone) % 2 == 0: # even len -> split 
    m = len(stone) // 2
    left_part, right_part = stone[:m], stone[m:]
    right_part = str(int(right_part))
    
    return apply_rules_recursive(left_part, iteration - 1) + \
           apply_rules_recursive(right_part, iteration - 1)
  
  return apply_rules_recursive(str(int(stone) * 2024), iteration - 1)  # stone * 2024


def part_one(stones: list[str]) -> int:
  return sum(apply_rules_recursive(stone, 25) for stone in stones)


def part_two(stones: list[str]) -> int:
  return sum(apply_rules_recursive(stone, 75) for stone in stones)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input = read_file(sys.argv[1])
  pr("Part One:", part_one(input))
  pr("Part Two:", part_two(input))
  