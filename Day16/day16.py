
import sys
sys.setrecursionlimit(9999)

MOVES : dict = {
  '.': {
      'u': [(-1, 0, 'u')],
      'd': [(1, 0, 'd')],
      'l': [(0, -1, 'l')],
      'r': [(0, 1, 'r')],
    },
  '/': {
      'u': [(0, 1, 'r')],
      'd': [(0, -1, 'l')],
      'l': [(1, 0, 'd')],
      'r': [(-1, 0, 'u')],
    },
  '\\': {
      'u': [(0, -1, 'l')],
      'd': [(0, 1, 'r')],
      'l': [(-1, 0, 'u')],
      'r': [(1, 0, 'd')],
    },
  '|': {
      'u': [(-1, 0, 'u')],
      'd': [(1, 0, 'd')],
      'l': [(1, 0, 'd'), (-1, 0, 'u')],
      'r': [(1, 0, 'd'), (-1, 0, 'u')],
    },
  '-': {
      'u': [(0, 1, 'r'), (0, -1, 'l')],
      'd': [(0, 1, 'r'), (0, -1, 'l')],
      'l': [(0, -1, 'l')],
      'r': [(0, 1, 'r')],
    },
}

State = tuple[int, int, str]

cavern = open('./input.txt').read().splitlines()
rows = len(cavern)
cols = len(cavern[0])
start : State = (0, 0, 'r')

seen : set = set()
energized_cells : set = set()
def beam_path(curr: State) -> None:
  seen.add(curr)
  i, j, dir = curr
  cell_type = cavern[i][j]
  
  if (i, j) not in energized_cells:
    energized_cells.add((i, j))

  for ii, jj, nd in MOVES[cell_type][dir]:
    ni, nj = i+ii, j+jj
    if 0 <= ni < rows and 0 <= nj < cols and (ni, nj, nd) not in seen:
      beam_path((ni, nj, nd)) 

beam_path(start)
print(f'Part One Answer: {len(energized_cells)}')

res = 0
for i, j, d in [(0, 0, 'd'), (rows-1, 0, 'u'), (0, 0, 'r'), (0, cols-1, 'l')]:
  for s in range(cols):
    seen : set = set()
    energized_cells : set = set()
    beam_path((0, s, d) if d in ['u', 'd'] else (s, 0, d))
    res = max(len(energized_cells), res)

print(f'Part Two Answer: {res}')
