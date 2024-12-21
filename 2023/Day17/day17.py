from heapq import heappop, heappush
import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 
 
Coord = tuple[int, int]

fac2dir = {
  ">": (0, 1),
  "^": (-1, 0),
  "<": (0, -1),
  "v": (1, 0),
}

facNDir = {
  ">": [(1, 0, "v"), (-1, 0, "^")],
  "^": [(0, 1, ">"), (0, -1, "<")],
  "<": [(1, 0, "v"), (-1, 0, "^")],
  "v": [(0, 1, ">"), (0, -1, "<")],
}
def part_one(maze: list[str]) -> int:
  n, m = len(maze), len(maze[0])
  maze = list(map(lambda x: list(map(int, list(x))), maze))
  end = (n-1, m-1)
  
  #      total i  j   f   c
  stack = [(0, 0, 0, ">", 1)]
  visited: dict[tuple[Coord, str, int], int] = {}
  while stack:
    total, i, j, f, c = heappop(stack)
    
    if (i, j) == end:
      return total
    
    if ((i, j), f, c) in visited and visited[((i, j), f, c)] <= total:
      continue
    visited[((i, j), f, c)] = total
    
    if c < 3:
      di, dj = fac2dir[f]
      ni, nj = i+di, j+dj
      if 0 <= ni < n and  0 <= nj < m:
        heappush(stack, (total + maze[ni][nj], ni, nj, f, c+1))
    
    for di, dj, nf in facNDir[f]:
      ni, nj = i+di, j+dj
      if 0 <= ni < n and 0 <= nj < m:
        heappush(stack, (total + maze[ni][nj], ni, nj, nf, 1))
  
  return -1


def part_two(maze: list[str]) -> int:
  n, m = len(maze), len(maze[0])
  maze = list(map(lambda x: list(map(int, list(x))), maze))
  end = (n-1, m-1)
  
  #      total i  j   f   c
  stack = [(0, 0, 0, ">", 1)]
  visited: dict[tuple[Coord, str, int], int] = {}
  mmin = float('inf')
  while stack:
    total, i, j, f, c = heappop(stack)
    
    if (i, j) == end and c >= 4:
      mmin = min(mmin, total)
    
    if (i, j) in visited and visited[(i, j)] <= total:
      continue
    visited[(i, j)] = total
    
    if c <= 10:
      di, dj = fac2dir[f]
      ni, nj = i+di, j+dj
      if 0 <= ni < n and  0 <= nj < m:
        heappush(stack, (total + maze[ni][nj], ni, nj, f, c+1))
    
    if c >= 4:
      for di, dj, nf in facNDir[f]:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m:
          heappush(stack, (total + maze[ni][nj], ni, nj, nf, 1))
        
  return mmin


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  