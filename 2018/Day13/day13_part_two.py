

with open("input.txt", "r") as fr:
  lines = fr.read().strip().split("\n")


auto_dir = {
  '^': (-1, 0),
  'v': (+1, 0),
  '<': (0, -1),
  '>': (0, +1),
}

mv_lft = {
  '>': '^',
  '^': '<',
  '<': 'v',
  'v': '>',
}

mv_right = {
  '>': 'v',
  'v': '<',
  '<': '^',
  '^': '>',
}

mv_st = {
  '>': '>',
  'v': 'v',
  '<': '<',
  '^': '^',
}

inter_mov = [mv_lft, mv_st, mv_right]

cars = {}
for i, line in enumerate(lines):
  for j, val in enumerate(line):
    if val in auto_dir:
      cars[(i, j)] = [0, val]
      

def show_cross(cross: list[list[str]], iter="#"):
  cross_cp = [[val for val in row] for row in cross]
  
  for (i, j), (_, car) in cars.items():
    if cross_cp[i][j] not in auto_dir:
      cross_cp[i][j] = car  
    else:
      cross_cp[i][j] = "X"  
      
  print("=" * 10, iter, "=" * 10)
  for row in cross_cp:
    print(*row)
  print()
  print("=" * 23)
  
  
def sum_coord(p1, p2):
  i, j = p1
  ii, jj = p2
  return i + ii, j + jj

def make_move(i, j, inter_i, car_dir) -> tuple[int, int, int, str]:
  coord_val = crossroad[i][j]
  new_inter_i = inter_i
  
  match coord_val:
    case "|" | "-":
      ni, nj = sum_coord((i, j), auto_dir[car_dir])
      nxt_car_dir = car_dir
    
    case "\\":
      if car_dir == "^":
        nxt_car_dir = "<"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
      
      elif car_dir == ">":
        nxt_car_dir = "v"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
      
      elif car_dir == "<":
        nxt_car_dir = "^"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
        
      elif car_dir == "v":
        nxt_car_dir = ">"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
    
    case "/":
      if car_dir == "^":
        nxt_car_dir = ">"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
      
      elif car_dir == ">": 
        nxt_car_dir = "^"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
        
      elif car_dir == "<": 
        nxt_car_dir = "v"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
        
      elif car_dir == "v": 
        nxt_car_dir = "<"
        ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
    
    case "+":
      nxt_car_dir = inter_mov[inter_i][car_dir]
      new_inter_i = (inter_i + 1) % len(inter_mov)
      ni, nj = sum_coord((i, j), auto_dir[nxt_car_dir])
  
  return ni, nj, new_inter_i, nxt_car_dir

crossroad = [list(line) for line in lines]
for i, row in enumerate(crossroad):
  for j, val in enumerate(row):
    if val in ["^", "v"]:
      crossroad[i][j] = "|"
    
    elif val in ["<", ">"]:
      crossroad[i][j] = "-"
    
# show_cross(crossroad, 0)

tick = 1
while len(cars) > 1:
  
  for i, j in sorted(list(cars.keys())):
    if (i, j) not in cars:
      continue
    
    inter_i, car_dir = cars[(i, j)]
    
    ni, nj, new_inter_i, new_car_dir = make_move(
      i, j, inter_i, car_dir
    )  
    
    if (ni, nj) in cars:
      crash_found = True
      del cars[(i, j)]
      del cars[(ni, nj)]
      continue
    
    del cars[(i, j)]
    cars[(ni, nj)] = new_inter_i, new_car_dir
  
  # show_cross(crossroad, tick)
  tick += 1
    
print(f"Part Two: {nj},{ni}")
