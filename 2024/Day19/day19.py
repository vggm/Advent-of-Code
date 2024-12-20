from functools import cache
import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip()


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

def get_params(lines: str) -> tuple[set[str], list[str]]:
  patterns, designs = lines.split("\n\n")
  
  patterns = set(patterns.strip().split(", "))
  designs = designs.split("\n")
  
  return patterns, designs
  

@cache
def possibilities(e: int, curr: str, design: str) -> int:
  global patterns
  
  if e == len(design):
    return len(curr) == 0 # True add 1, False add 0
  
  total = 0
  for i, c in enumerate(design[e:], start=e):
    curr += c
    if curr in patterns:
      total += possibilities(i+1, '', design)
  
  return total
  

def part_one(file_input: list[str]) -> int:
  global patterns
  patterns, designs = get_params(file_input)
  return sum(possibilities(0, '', design) > 0 for design in designs)


def part_two(file_input: list[str]) -> int:
  global patterns
  patterns, designs = get_params(file_input)
  return sum(possibilities(0, '', design) for design in designs)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  