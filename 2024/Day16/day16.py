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
  
  visited: dict[Coord, int] = {}
  stack = [(0, "e", i, j)]
  while stack:
    d, f, i, j = heappop(stack)
    
    if (i, j) == end:
      return d

    if (i, j, f) in visited and visited[(i, j, f)] <= d:
      continue
    visited[(i, j, f)] = d
    
    di, dj = face2dir[f]
    ni, nj = i+di, j+dj
    if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != WALL:
      if (ni, nj, f) not in visited or visited[(ni, nj, f)] > d:
        heappush(stack, (d+1, f, ni, nj))
    
    for di, dj, nf in nextDir[f]:
      ni, nj = i+di, j+dj
      if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != WALL:
        if (i, j, nf) not in visited or visited[(i, j, nf)] > d:
          heappush(stack, (d+1000, nf, i, j))
       
  return -1


def part_two(maze: list[str]) -> int:
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  # pr("Part Two:", part_two(file_input))
  
