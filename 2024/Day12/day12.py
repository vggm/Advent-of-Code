from collections import defaultdict
import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)


Coord = tuple[int, int]


class Region:
  area: int = 0
  side: int = 0
  perimeter: int = 0
  corner: set[Coord] = set()
  contour: set[Coord] = set()
  contour_freq: defaultdict[int] = defaultdict(int)
  
  def calculate_sides(self) -> int:
    print(self.contour)
    print(self.contour_freq)
    # contour = self.contour.copy()
    # side = 1
    
    # i, j = contour.pop()
    # while contour:
    #   for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
    #     if (ni, nj) in contour:
          
    #       i, j = ni, nj
          
 

def part_one(garden: list[str]) -> int:
  n, m = len(garden), len(garden[0])
  
  visited: set[Coord] = set()
  def dfs(i: int, j: int, region: Region):
    region.area += 1
    visited.add((i, j))
    
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
      if (ni < 0 or ni == n or nj < 0 or nj == m) or garden[ni][nj] != garden[i][j]:
        region.perimeter += 1
        continue
      
      if (ni, nj) not in visited:
        dfs(ni, nj, region)  
  
  total_price = 0
  for i, row in enumerate(garden):
    for j, _ in enumerate(row):        
      if (i, j) not in visited:
        region = Region()
        dfs(i, j, region)
        total_price += region.area * region.perimeter
  
  return total_price


def part_two(garden: list[str]) -> int:
  n, m = len(garden), len(garden[0])
    
  visited: set[Coord] = set()
  def dfs(i: int, j: int, contour: Region):
    visited.add((i, j))
    region.area += 1
    
    # check diagonally
    for ni, nj in [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
      if (ni < 0 or ni == n or nj < 0 or nj == m) or garden[ni][nj] != garden[i][j]:
        region.contour.add((ni, nj))
        region.contour_freq[(ni, nj)] += 1
    
    # check neighbour
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
      if (ni < 0 or ni == n or nj < 0 or nj == m) or garden[ni][nj] != garden[i][j]:
        region.contour.add((ni, nj))
        region.contour_freq[(ni, nj)] += 1
        region.perimeter += 1
        continue
      
      if (ni, nj) not in visited:
        dfs(ni, nj, contour)  
  
  total_price = 0
  for i, row in enumerate(garden):
    for j, _ in enumerate(row):        
      if (i, j) not in visited:
        region = Region()
        dfs(i, j, region)
        region.calculate_sides()
        # total_price += region.area * region.side
  
  return total_price


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  for filename in sys.argv[1:]:
    print(f"Filename: [ {filename} ]")
    input = read_file(filename)
    pr("Part One:", part_one(input))
    pr("Part Two:", part_two(input))
    print()
  