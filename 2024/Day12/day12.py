import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)


Coord = tuple[int, int]


class Region:
  
  def __init__(self, letter="#"):
    self.area: int = 0
    self.letter: str = letter
    self.total_sides: int = 0
        
    self.perimeter: int = 0
    self.structure: set[Coord] = set()
    
    self.top: set[Coord] = set()
    self.left: set[Coord] = set()
    self.right: set[Coord] = set()
    self.bottom: set[Coord] = set()
    
    self.matrix = None
    
  def _calculate_extremes(self) -> tuple[int, int, int, int]:
    
    mmi, mmj, mxi, mxj = float('inf'), float('inf'), -float('inf'), -float('inf')
    for i, j in self.structure:
      mmi, mmj = min(mmi, i), min(mmj, j)
      mxi, mxj = max(mxi, i), max(mxj, j)
    
    return mmi, mmj, mxi, mxj
  
  def draw(self):

    mmi, mmj, mxi, mxj = self._calculate_extremes()
    idiff, jdiff = mmi, mmj
    
    matrix = [[' ' for _ in range(mxj-mmj+1)] for _ in range(mxi-mmi+1)]
    for i, j in self.structure:
      i, j = i-idiff, j-jdiff
      matrix[i][j] = self.letter
    
    print("\n+", "-" * (mxj-mmj+1), "+")
    for row in matrix:
      line = "| "
      for val in row:
        line += val
      print(line, "|")
    print("+", "-" * (mxj-mmj+1), "+", "\n")
  
  def calculate_sides(self) -> int:
    print("Area:", self.area)
    print("Structure:", self.structure)
  
    sides: list[set[Coord]] = [] 
    #                      top      bot    left     right
    for chk_i, chk_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      side_dir: set[Coord] = set()
      for i, j in self.structure:
        if (i+chk_i, j+chk_j) not in self.structure:
          side_dir.add((i, j))
      sides.append(side_dir.copy())
      
    print(sides)
    
    for side in sides:
      while side:
        i, j = side.pop()
        
        neighbours: set[Coord] = set([(i, j)])
        while neighbours:
          i, j = neighbours.pop()
          if (i, j) in side:
            side.remove((i, j))
          for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if (ni, nj) in side:
              neighbours.add((ni, nj))
        
        self.total_sides += 1
    
    print("Total sides:", self.total_sides, "\n")
    return self.total_sides
    
          
 

def part_one(garden: list[str]) -> int:
  n, m = len(garden), len(garden[0])
  
  visited: set[Coord] = set()
  def dfs(i: int, j: int, region: Region):
    region.structure.add((i, j))
    visited.add((i, j))
    region.area += 1
    
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
      if (ni < 0 or ni == n or nj < 0 or nj == m) or garden[ni][nj] != garden[i][j]:
        region.perimeter += 1
        continue
      
      if (ni, nj) not in visited:
        dfs(ni, nj, region)  
  
  total_price = 0
  for i, row in enumerate(garden):
    for j, letter in enumerate(row):        
      if (i, j) not in visited:
        region = Region(letter)
        dfs(i, j, region)
        total_price += region.area * region.perimeter
  
  return total_price


def part_two(garden: list[str]) -> int:
  n, m = len(garden), len(garden[0])
    
  visited: set[Coord] = set()
  def dfs(i: int, j: int, contour: Region):
    region.structure.add((i, j))
    visited.add((i, j))
    region.area += 1
    
    # check neighbour
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
      if (ni < 0 or ni == n or nj < 0 or nj == m) or garden[ni][nj] != garden[i][j]:
        region.perimeter += 1
        continue
      
      if (ni, nj) not in visited:
        dfs(ni, nj, contour)  
  
  total_price = 0
  for i, row in enumerate(garden):
    for j, letter in enumerate(row):        
      if (i, j) not in visited:
        region = Region(letter)
        dfs(i, j, region)
        region.draw()
        region.calculate_sides()
        total_price += region.area * region.total_sides
  
  return total_price


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  # filename = "./test2.in"
  for filename in sys.argv[1:]:
    print(f"Filename: [ {filename} ]")
    input = read_file(filename)
    pr("Part One:", part_one(input))
    pr("Part Two:", part_two(input))
    print()
  