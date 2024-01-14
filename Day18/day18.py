
import sys
from itertools import pairwise
sys.setrecursionlimit(99999) # expand method doesn't work without this conf


Point = tuple[int, int]


moves = {
  'R': lambda i, j, s: (i, j+s),
  'D': lambda i, j, s: (i+s, j),
  'L': lambda i, j, s: (i, j-s),
  'U': lambda i, j, s: (i-s, j),
}


def normalize(num: int) -> int:
  if num < 0:
    return -1
  elif num > 0:
    return 1
  else:
    return 0


def print_digplan(dig_plan: list[str]) -> None:
  with open('out.txt', 'w') as out:
    for row in dig_plan:
      out.write(row + '\n')


plan = open('./input.txt').read().splitlines()

i, j = 0, 0
top, bottom, left, right = 0, 0, 0, 0
for move, steps, _ in list(map(lambda s: s.split(), plan)):
  i, j = moves[move](i, j, int(steps))
  top = max(i, top)
  left = min(j, left)
  right = max(j, right)
  bottom = min(i, bottom)
  
rows = top - bottom + 1
cols = right - left + 1
start: Point = rows - 1 - top, cols - 1 - right
center: Point = rows // 2, cols // 2 # the center must be inside the polygon

print(f'Rows: {rows}, Cols: {cols}, Start: {start}, Center: {center}')

dig_plan = [''.join('.' for _ in range(cols)) for _ in range(rows)]

i, j = start
perimeter = 0
for move, steps, _ in list(map(lambda s: s.split(), plan)):
  ni, nj = moves[move](i, j, int(steps))
  ci, cj = ni-i, nj-j

  while (i, j) != (ni, nj):    
    perimeter += 1
    dig_plan[i] = dig_plan[i][:j] + '#' + dig_plan[i][j+1:]
    i, j = i + normalize(ci), j + normalize(cj)

print_digplan(dig_plan)

def expand(curr: Point) -> int:
  i, j = curr
  
  if dig_plan[i][j] == '#':
    return 0
  
  res = 0
  dig_plan[i] = dig_plan[i][:j] + '#' + dig_plan[i][j+1:]
  for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
    if 0 <= ni < rows and 0 <= nj < cols and dig_plan[ni][nj] != '#':
      res += expand((ni, nj))
  
  return res + 1

ans = expand(center) + perimeter
print(f'Part One Answer: {ans}')
    
# Solving with Shoelace Formula and Pick's Theorem
# Part One

grid = open('./input.txt').read().splitlines()
points : list[Point] = [(0, 0)]

i, j = 0, 0
for move, steps, _ in list(map(lambda s: s.split(), grid)):
  i, j = moves[move](i, j, int(steps))
  points.append((i, j))

# print(f'Vertices: {points}')

# The next 2 lines could be just one for-loop, but i wanted to separate the two math formulas for more legibility
P = sum(abs(r1-r2) + abs(c1-c2) for (r1, c1), (r2, c2) in pairwise(points)) # Perimeter
A = abs(sum(r1 * c2 - r2 * c1 for (r1, c1), (r2, c2) in pairwise(points))) / 2 # Shoelace Formula

print()
print(f'Area: {A}')
print(f'Perimeter: {P}')
ans = int(A - P/2 + 1) + P # Pick's theorem
print(f'Part One Answer: {ans}')

# Part Two
P = 0
i, j = 0, 0
points : list[Point] = [(0, 0)]
for _, _, hex_code in list(map(lambda s: s.split(), grid)):
  hex_code = hex_code[2:-1]
  steps = int(hex_code[:-1], 16)
  move = list(moves.keys())[int(hex_code[-1])]
  
  i, j = moves[move](i, j, steps)
  points.append((i, j))
  
  P += steps

A = abs(sum(r1 * c2 - r2 * c1 for (r1, c1), (r2, c2) in pairwise(points))) / 2 # Shoelace Formula

print()
print(f'Area: {A}')
print(f'Perimeter: {P}')
ans = int(A - P/2 + 1) + P # Pick's theorem  
print(f'Part Two Answer: {ans}')
