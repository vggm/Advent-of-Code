
from typing import Counter


def read_file(filename: str) -> list[str]:
  with open(filename, 'r') as rfile:
    return rfile.readlines()


WORD = 'XMAS'
DIR = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
def part_one(matrix: list[str]) -> int:
  n, m = len(matrix), len(matrix[0])
    
  def continue_path(i, j, dir, wrd) -> bool:
    if wrd == WORD:
      return True
  
    k = len(wrd)
    di, dj = dir
    ni, nj = i+di, j+dj
    if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == WORD[k]:
      if continue_path(ni, nj, dir, wrd + matrix[ni][nj]):
        return True
    
    return False
  
  total = 0
  for i, row in enumerate(matrix):  
    for j, val in enumerate(row):
      if val == 'X':
        for dir in DIR:
          total += continue_path(i, j, dir, 'X')
        
  return total


def part_two(mx: list[str]) -> int:
  n, m = len(mx), len(mx[0])
  
  def check_X(i, j):
    xmass = Counter('MMSS')
    tl, tr, bl, br = mx[i-1][j-1], mx[i-1][j+1], mx[i+1][i-1], mx[i+1][j+1]
    return Counter(tl+tr+bl+br) == xmass
  
  total = 0
  for i, row in enumerate(mx):  
    for j, val in enumerate(row):
      if val == 'A':
        if (0 <= i-1 and i+1 < n) and (0 <= j-1 and j+1 < m):
          total += check_X(i, j)
        
  return total


if __name__ == '__main__':
  test = read_file("./test1.in")
  
  sol = part_one(test)
  assert sol == 18, f"Expected 18, but got {sol}."
  
  in1 = read_file("./in1.in")
  print(f"Part One: {part_one(in1)}")
  
  sol = part_two(test)
  assert sol == 9, f"Expected 9, but got {sol}."
  
  print(f"Part Two: {part_two(in1)}")  
