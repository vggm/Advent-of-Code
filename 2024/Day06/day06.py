

def read_file(filename: str) -> list[str]:
  with open(filename, "r") as rfile:
    lines = []
    
    line = rfile.readline().removesuffix("\n")
    while line != '':
      lines.append(line)
      line = rfile.readline().removesuffix("\n")
      
    return lines
  

def get_guard_coords(maze: list[str]) -> tuple[int, int]:
  for i, row in enumerate(maze):
    for j, val in enumerate(row):
      if val == GUARD:
        return i, j  

  return -1, -1


WALL, GUARD = "#", "^"
DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def part_one(maze: list[str]) -> int:
  maze = list(map(lambda s: s.removesuffix("\n"), maze))
  
  n, m = len(maze), len(maze[0])
  i, j = get_guard_coords(maze)
    
  seen = set()
  curr_dir = 0
  di, dj = DIR[0]
  while 0 <= i < n and 0 <= j < m:
    seen.add((i, j))

    ni, nj = i + di, j + dj
    if not(0 <= ni < n and 0 <= nj < m):
      break
    
    if maze[ni][nj] == WALL:
      curr_dir = (curr_dir + 1) % len(DIR)
      di, dj = DIR[curr_dir]
      ni, nj = i+di, j+dj
    
    i, j = ni, nj
      
  return len(seen)


def check_loop(curr_dir: int, obstacle: tuple[int, int], maze: list[str]) -> bool:
  n, m = len(maze), len(maze[0])
  oi, oj = obstacle
  di, dj = DIR[curr_dir]
  i, j = oi-di, oj-dj
  
  if maze[oi][oj] == WALL:
    return False
  
  maze[oi][oj] = WALL
  visited = set()
  
  while 0 <= i < n and 0 <= j < m:
    if (i, j, curr_dir) in visited: # loop found 
      maze[oi][oj] = '.'
      return True

    if maze[i][j] == WALL:
      print('hotia')
    visited.add((i, j, curr_dir))
    
    ni, nj = i+di, j+dj
    if not(0 <= ni < n and 0 <= nj < m):
      break 
    
    while maze[ni][nj] == WALL:
      curr_dir = (curr_dir + 1) % len(DIR)
      di, dj = DIR[curr_dir]
      ni, nj = i+di, j+dj
    
    i, j = ni, nj
  
  maze[oi][oj] = '.'
  return False
    

def part_two(maze: list[str]) -> int:
  maze = list(map(lambda s: [x for x in s], maze))
  n, m = len(maze), len(maze[0])
  i, j = get_guard_coords(maze)
    
  curr_dir = 0
  di, dj = DIR[0]
  obstacle_seen = set()
  while 0 <= i < n and 0 <= j < m:
    ni, nj = i + di, j + dj
    if not(0 <= ni < n and 0 <= nj < m):
      break
      
    if maze[ni][nj] == WALL:
      curr_dir = (curr_dir + 1) % len(DIR)
      di, dj = DIR[curr_dir]
      ni, nj = i+di, j+dj
    
    else:
      if (i, j) not in obstacle_seen and check_loop(curr_dir, (ni, nj), maze):
        obstacle_seen.add((i, j))
    
    i, j = ni, nj
    
  return len(obstacle_seen)


if __name__ == '__main__':
  test = read_file("./test.in")
  
  sol = part_one(test)
  assert sol == 41, f"Expected 41, but got {sol}."
  
  in1 = read_file("./in1.in")
  print(f"Part One: {part_one(in1)}")
  
  sol = part_two(test)
  assert sol == 6, f"Expected 6, but got {sol}."
  
  print(f"Part Two: {part_two(in1)}")
  