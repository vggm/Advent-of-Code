
grid = open('./input.txt').read().splitlines()

start = (0, 1)
end = (len(grid)-1, len(grid[0])-2)

points = {start, end}

for i, row in enumerate(grid):
  for j, v in enumerate(row):
    if v == '#':
      continue
    
    neighbors = 0
    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
      if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != '#':
        neighbors += 1
      
    if neighbors >= 3:
      points.add((i, j))

graph = {}
def clear_graph():
  global graph
  graph = {pt: {} for pt in points}
clear_graph()

dirs = {
  '^': [(-1, 0)],
  'v': [(1, 0)],
  '<': [(0, -1)],
  '>': [(0, 1)],
  '.': [(1, 0), (-1, 0), (0, 1), (0, -1)]
}

def make_graph(part: int):
  for si, sj in points:
    stack = [(0, si, sj)]
    seen = {(si, sj)}
    
    while stack:
      n, i, j = stack.pop()
      
      if n != 0 and (i, j) in points:
        graph[(si, sj)][(i, j)] = n
        continue
      
      for y, x in dirs[grid[i][j]] if part == 1 else dirs['.']:
        ni, nj = i+y, j+x
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != '#' and (ni, nj) not in seen:
          stack.append((n+1, ni, nj))
          seen.add((ni, nj))
        
seen = set()
def dfs(pt: tuple[int, int]) -> int:
  if pt == end:
    return 0
  
  m = -float('inf')
  
  seen.add(pt)
  for nxt in graph[pt]:
    if nxt not in seen:
      m = max(m, dfs(nxt) + graph[pt][nxt])
  seen.remove(pt)  
  
  return m

make_graph(part=1)
print(f'Part One: {dfs(start)}')

seen.clear()
clear_graph()
make_graph(part=2)
print(f'Part Two: {dfs(start)}')