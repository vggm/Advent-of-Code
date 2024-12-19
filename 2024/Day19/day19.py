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
  
  
def is_possible_bt(e: int, curr: str, design: str, patterns: set[str]) -> int:
  if e == len(design):
    pass
  
  total = 0
  for i, c in enumerate(design[e:]):
    if curr + c in patterns:
      total += is_possible_bt(i+1, '', design, patterns)
    
    total += is_possible_bt(e+1, curr + c, design, patterns)
  
  
def is_possible(design: str, patterns: set[str], p1=True) -> int:
  step_back = []
  found = 0
  
  seen = set()
  start, end = 0, 1
  while end <= len(design) or step_back:

    if end >= len(design)+1:
      start, end = step_back.pop()
      
    if end <= len(design) and design[start:end] in patterns and (start, end) not in seen:
      seen.add((start, end))
      step_back.append((start, end+1))
      start = end
      
    if start == len(design):
      found += 1
      end = len(design)+1
      
      if p1:
        return found
      
      continue
    
    end += 1
  
  return found
  

def part_one(file_input: list[str]) -> int:
  patterns, designs = get_params(file_input)
  return sum(is_possible(design, patterns)>0 for design in designs)


def part_two(file_input: list[str]) -> int:
  patterns, designs = get_params(file_input)
  return sum(is_possible(design, patterns, p1=False) for design in designs)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  
