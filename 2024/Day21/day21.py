from collections import deque
from heapq import heappop, heappush
import sys
import pyperclip as cp
import rich as rh


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
  
  
  
possible_dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir2move = [">", "<", "v", "^"]

numeric_keypad = [
  "789",
  "456",
  "123",
  "#0A"
]

directional_keypad = [
  "#^A",
  "<v>"
]
 

def make_all_numeric_paths() -> dict[str, dict[str, str]]:
  global numeric_keypad
  n, m = len(numeric_keypad), len(numeric_keypad[0])
  
  numeric_path: dict[str, dict[str, str]] = {}
  for ii, row in enumerate(numeric_keypad):
    for jj, val in enumerate(row):
      
      if val == "#": continue
      
      numeric_path[val] = {}
      
      visited = {}
      stack = [(0, ii, jj, "", -1)]
      while stack:
        d, i, j, path, dir = heappop(stack)
        
        if (i, j) in visited and visited[(i, j)] < d:
          continue
        
        visited[(i, j)] = d
        numeric_path[val][numeric_keypad[i][j]] = path
        
        for ndir, (di, dj) in enumerate(possible_dirs):
          ni, nj = i+di, j+dj
          if 0 <= ni < n and 0 <= nj < m and numeric_keypad[ni][nj] != "#":
            cost = 1
            
            if ndir != 1:
              cost += 50
              
            heappush(stack, (d + cost, ni, nj, path + dir2move[ndir], ndir))
      
  return numeric_path


def make_all_directional_paths() -> dict[str, dict[str, str]]:
  global directional_keypad
  n, m = len(directional_keypad), len(directional_keypad[0])
  
  directional_path: dict[str, dict[str, str]] = {}
  for ii, row in enumerate(directional_keypad):
    for jj, val in enumerate(row):
      
      if val == "#": continue
      
      directional_path[val] = {}
      
      visited = {}
      stack = [(0, ii, jj, "", -1)]
      while stack:
        step, i, j, path, dir = heappop(stack)
        
        if (i, j) in visited and visited[(i, j)] < step:
          continue
        
        visited[(i, j)] = step
        directional_path[val][directional_keypad[i][j]] = path
        
        for ndir, (di, dj) in enumerate(possible_dirs):
          ni, nj = i+di, j+dj
          if 0 <= ni < n and 0 <= nj < m and directional_keypad[ni][nj] != "#":
            cost = 1
            
            if dir != ndir:
              cost += 10
              
            if dir != 0:
              cost += 10
            
            heappush(stack, (step + cost, ni, nj, path + dir2move[ndir], ndir))

  return directional_path

def make_all_paths() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
  numeric_path = make_all_numeric_paths()
  directional_path = make_all_directional_paths()
  return numeric_path, directional_path


def part_one(codes: list[str]) -> int:
  num_path, dir_path = make_all_paths()
  
  rh.print(num_path)
  rh.print(dir_path)
  
  ans = 0
  for code in codes:
    
    print(f"\n{code}:")
    start, path = "A", ""
    for end in code:
      path += num_path[start][end] + "A"
      start = end
    print(path)
    
    # first robot
    start, ft_bot = "A", ""
    for end in path:
      ft_bot += dir_path[start][end] + "A"
      start = end
    print(ft_bot)
    
    # second robot
    start, nd_bot = "A", ""
    for end in ft_bot:
      nd_bot += dir_path[start][end] + "A"
      start = end
    print(nd_bot)
    
    seq, num_part = len(nd_bot), int(code[:-1])
    print(seq, num_part)
    ans += seq * num_part
    
  return ans


def part_two(codes: list[str]) -> int:
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  # pr("Part Two:", part_two(file_input))
  