import sys
import pyperclip as cp
from heapq import heappop, heappush


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

Coord = tuple[int, int]
VOID, CORRUPTED = ".", "#"
def part_one(file_input: list[str], test: bool) -> int:
  coords = list(map(lambda x: list(map(int, x.split(","))), file_input))
  n = m = max(max(x, y) for x, y in coords) + 1
  
  memory = [[VOID for _ in range(m)] for _ in range(n)]
  for j, i in coords[:(1024 if not test else 12)]:
    memory[i][j] = CORRUPTED
      
  visited: dict[Coord, int] = {}
  stack = [(0, 0, 0)]
  while stack:
    step, i, j = heappop(stack)
    
    if (i, j) == (n-1, m-1):
      return step
    
    if (i, j) in visited and visited[(i, j)] <= step:
      continue
    visited[(i, j)] = step
    
    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
      if 0 <= ni < n and 0 <= nj < m and memory[ni][nj] != CORRUPTED:
        heappush(stack, (step+1, ni, nj))
  
  return -1


def part_two(file_input: list[str]) -> int:
  coords = list(map(lambda x: list(map(int, x.split(","))), file_input))
  n = m = max(max(x, y) for x, y in coords) + 1
  
  memory = [[VOID for _ in range(m)] for _ in range(n)]
  for j, i in coords:
    memory[i][j] = CORRUPTED
      
  for coord in coords[::-1]:
    j, i = coord
    memory[i][j] = VOID
    
    visited: dict[Coord, int] = {}
    stack = [(0, 0, 0)]
    while stack:
      step, i, j = heappop(stack)
      
      if (i, j) == (n-1, m-1):
        return f"{coord[0]},{coord[1]}"
      
      if (i, j) in visited and visited[(i, j)] <= step:
        continue
      visited[(i, j)] = step
      
      for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= ni < n and 0 <= nj < m and memory[ni][nj] != CORRUPTED:
          heappush(stack, (step+1, ni, nj))
  
  return ""


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input, sys.argv[1].startswith("test")))
  pr("Part Two:", part_two(file_input))
  
