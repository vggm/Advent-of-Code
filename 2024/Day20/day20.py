from collections import defaultdict, deque
import pyperclip as cp
import sys


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 
 
Coord = tuple[int, int]
def get_params(maze: list[str]) -> tuple[Coord, Coord]:
  start, end = None, None
  for i, row in enumerate(maze):
    for j, val in enumerate(row):
      if val == "S":
        start = i, j
      
      elif val == "E":
        end = i, j
  
  return start, end


def make_path(maze: list[str]) -> tuple[list[tuple[Coord, int]], dict[Coord, int]]: 
  n, m = len(maze), len(maze[0])
  
  (i, j), end = get_params(maze)
  
  stack = deque([(0, i, j)])
  path: list[tuple[Coord, int]] = []
  visited: dict[Coord, int] = {(i, j): 0}
  while stack:
    s, i, j = stack.pop()
    path.append(((i, j), s))

    if (i, j) == end:
      break     
    
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
      if 0 <= ni < n and 0 <= nj < m \
        and maze[ni][nj] != "#" \
        and (ni, nj) not in visited:
          visited[(ni, nj)] = s+1
          stack.append((s+1, ni, nj))
  
  return path, visited


def solve(maze: list[str]):
  n, m = len(maze), len(maze[0])
  path, visited = make_path(maze)
  
  # PART 1
  saves: defaultdict[int] = defaultdict(int)
  for (i, j), ps in path:
    for ni, nj in [(i+2, j), (i-2, j), (i, j+2), (i, j-2)]:
      if 0 <= ni < n and 0 <= nj < m\
        and (ni, nj) in visited \
        and visited[(ni, nj)] > (ps + 2):
          saves[visited[(ni, nj)] - (ps+2)] += 1
  
  pr("Part One", sum(cnt for ps_saved, cnt in saves.items() if ps_saved >= 100))
  
  # PART 2
  saves: defaultdict[int] = defaultdict(int)
  for (i, j), ps in path:
    for ni in range(i-20, i+20+1):
      for nj in range(j-20, j+20+1):
        if 0 <= ni < n and 0 <= nj < m and (ni, nj) in visited:
          d = abs(ni-i) + abs(nj-j)
          if d > 20:
            continue
          
          if visited[(ni, nj)] > (ps + d):
            saves[visited[(ni, nj)] - (ps + d)] += 1
  
  pr("Part Two", sum(cnt for ps_saved, cnt in saves.items() if ps_saved >= 100))
  
  
if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  solve(file_input)
  