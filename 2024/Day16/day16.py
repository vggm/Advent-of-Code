from heapq import heappop, heappush
import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
  

Coord = tuple[int, int]
START, END, VOID, WALL = "S", "E", ".", "#"

  
def get_coords(maze: list[str]) -> tuple[Coord, Coord]:
  start, end = (-1, -1), (-1, -1)
  for i, row in enumerate(maze):
    for j, val in enumerate(row):
      if val == START:
        start = i, j
      elif val == END:
        end = i, j
  
  return start, end
 
 
nextDir = {
  "e": [(1, 0, "s"), (-1, 0, "n")],
  "n": [(0, 1, "e"), (0, -1, "o")],
  "o": [(1, 0, "s"), (-1, 0, "n")],
  "s": [(0, 1, "e"), (-1, 0, "o")]
}


face2dir = {
  "e": (0, 1),
  "n": (-1, 0),
  "o": (0, -1),
  "s": (1, 0)
}


def part_one(maze: list[str]) -> int:
  n, m = len(maze), len(maze[0])
  
  start, end = get_coords(maze)
  i, j = start
  
  stack = [(0, "e", i, j)]
  visited: dict[Coord, int] = {}
  while stack:
    d, f, i, j = heappop(stack)
    
    if (i, j) == end:
      return d

    if (i, j, f) in visited and visited[(i, j, f)] <= d:
      continue
    visited[(i, j, f)] = d
    
    di, dj = face2dir[f]
    ni, nj = i+di, j+dj
    if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != WALL \
      and ((ni, nj, f) not in visited or visited[(ni, nj, f)] > d):
        heappush(stack, (d+1, f, ni, nj))
    
    for di, dj, nf in nextDir[f]:
      ni, nj = i+di, j+dj
      if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != WALL \
        and ((i, j, nf) not in visited or visited[(i, j, nf)] > d):
          heappush(stack, (d+1000, nf, i, j))
       
  return -1


def part_two(maze: list[str]) -> int:
  n, m = len(maze), len(maze[0])
  
  start, end = get_coords(maze)
  i, j = start
  
  best_mark = float('inf')
  
  best_paths: set[Coord] = set()
  stack = [(0, "e", 0, i, j, set())]
  visited: dict[Coord, int] = {}
  while stack:
    d, f, step, i, j, path = heappop(stack)

    if (i, j) in visited and visited[(i, j)] < d:
      continue
    visited[(i, j, f)] = d
    
    if (i, j) == end and d <= best_mark:
      best_mark = d
      best_paths |= path | {end}
      continue
    
    di, dj = face2dir[f]
    ni, nj = i+di, j+dj
    if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != WALL \
      and ((ni, nj, f) not in visited or visited[(ni, nj, f)] >= d):
        heappush(stack, (d+1, f, step+1, ni, nj, path | {(i, j)}))
    
    for di, dj, nf in nextDir[f]:
      ni, nj = i+di, j+dj
      if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != WALL \
        and ((i, j, nf) not in visited or visited[(i, j, nf)] >= d):
          heappush(stack, (d+1000, nf, step, i, j, path))
       
  return len(best_paths)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  