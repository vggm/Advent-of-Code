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
  
  
  def __init__(self, letter="#"):
    self.area: int = 0
    self.side: int = 0
    self.letter: str = "#"
    self.perimeter: int = 0
    self.diagonal: set[Coord] = set()
    self.contour: set[Coord] = set()
    self.structure: set[Coord] = set()
    self.contour_freq: defaultdict[int] = defaultdict(int)

    self.tl, br = (0, 0), (0, 0)
    self.extremes_calculated = False

    self.matrix = None
    self.matrix_drew = False
    self.letter = letter
    
  def calculate_extremes(self) -> tuple[int, int, int, int]:
    if self.extremes_calculated:
      return *self.tl, *self.br
    self.extremes_calculated = True
    
    mmi, mmj, mxi, mxj = float('inf'), float('inf'), -float('inf'), -float('inf')
    for i, j in self.structure:
      mmi, mmj = min(mmi, i), min(mmj, j)
      mxi, mxj = max(mxi, i), max(mxj, j)
    
    self.tl = (mmi, mmj)
    self.br = (mxi, mxj)
    return mmi, mmj, mxi, mxj
  
  def draw(self, n=None, m=None):
    if n is not None and m is not None:
      matrix = [[0 for _ in range(m)] for _ in range(n)]
      for i, j in self.structure:
        matrix[i][j] = 1

    elif not self.matrix_drew:
      self.matrix_drew = True
      mmi, mmj, mxi, mxj = self.calculate_extremes()
      idiff, jdiff = mmi, mmj
      
      matrix = [[0 for _ in range(mxj+1)] for _ in range(mxi+1)]
      for i, j in self.structure:
        i, j = i-idiff, j-jdiff
        matrix[i][j] = 1
        
    for row in matrix:
      for val in row:
        print(' ' if not val else self.letter, end='')
      print()
  
  def calculate_sides(self) -> int:
    print("Diagonal:", self.diagonal)
    print("Contorno:", self.contour)
    print("Freq:", self.contour_freq)
    print("Corners Filtrado:", [(i, j) for (i, j), f in self.contour_freq.items() if f == 1 and (i, j) in self.diagonal])
    print("\n")
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
    
    # check diagonally
    for ni, nj in [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
      if (ni < 0 or ni == n or nj < 0 or nj == m) or garden[ni][nj] != garden[i][j]:
        region.diagonal.add((ni, nj))
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
    for j, letter in enumerate(row):        
      if (i, j) not in visited:
        region = Region(letter)
        dfs(i, j, region)
        region.draw(n, m)
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
  