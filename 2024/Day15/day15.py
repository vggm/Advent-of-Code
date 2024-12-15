import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

Coord = tuple[int, int]

ROBOT, BOX, WALL, VOID, DOUBLE_BOX = "@", "O", "#", ".", "[]"

dir2move: dict[str, Coord] = {
  "^": (-1, 0), # move up
  "<": (0, -1), # move left
  "v": (1, 0),  # move down
  ">": (0, 1)   # move right
}


def draw_matrix(house: list[list[str]]):
  for row in house:
    print(*row)
  print()


def define_params(input: list[str], draw: bool, p2=False) -> tuple[list[list[str]], str]:
  house, moves = input
  moves = moves.replace("\n", "")
  
  if p2:
    house = house.replace(".", "..").replace("#", "##").replace("O", "[]").replace("@", "@.")
  
  house = house.split("\n")
  house = list(map(list, house))
  
  if draw:
    for row in house:
      print(*row)
    # print(moves)
  
  return house, moves


def get_robot_coords(house: list[list[str]]) -> Coord:
  for i, row in enumerate(house):
    for j, val in enumerate(row):
      if val == ROBOT:
        return i, j
  
  return -1, -1


def make_move_p1(house: list[list[str]], start: Coord, mv: Coord) -> Coord:
  i, j = start

  if house[i][j] == WALL:
    return i, j
  
  di, dj = mv
  if house[i][j] == VOID:
    return i+di, j+dj
  
  pi, pj = make_move_p1(house, (i+di, j+dj), mv)
  ni, nj = pi-di, pj-dj
  
  house[i][j], house[ni][nj] = house[ni][nj], house[i][j]
  return ni, nj


def part_one(input: list[str], verbose: bool) -> int:
  house, moves = define_params(input, verbose)
  
  i, j = get_robot_coords(house)
  for move in moves:
    i, j = make_move_p1(house, (i, j), dir2move[move])
    
    # print("\nMove:", move)
    # draw_matrix(house)
  
  return sum( 100 * i + j for i, row in enumerate(house) for j, val in enumerate(row) if val == BOX)


def can_make_move(house: list[list[str]], start: Coord, mv: Coord) -> bool:
  i, j = start
  
  if house[i][j] == WALL:
    return False

  if house[i][j] == VOID:
    return True
  
  di, dj = mv
  if house[i][j] == ROBOT:
    return can_make_move(house, (i+di, j+dj), mv)
  
  # start is a double rock
  if not di: # move horizontally
    return can_make_move(house, (i, j+dj), mv)
    
  # move vertically
  if house[i][j] == "[":
    return can_make_move(house, (i+di, j), mv) \
        and can_make_move(house, (i+di, j+1), mv)
  # start is "]"
  return can_make_move(house, (i+di, j), mv) \
      and can_make_move(house, (i+di, j-1), mv)
        

def make_move(house: list[list[str]], start: Coord, mv: Coord) -> Coord:
  i, j = start

  if house[i][j] == VOID:
    return -1, -1
  
  di, dj = mv
  ni, nj = i+di, j+dj
  if di and house[i][j] in DOUBLE_BOX:
    nj = j+1 if house[i][j] == "[" else j-1

    make_move(house, (ni, j), mv)
    house[i][j], house[ni][j] = house[ni][j], house[i][j]
    
    make_move(house, (ni, nj), mv)
    house[i][nj], house[ni][nj] = house[ni][nj], house[i][nj]
    
    return ni, nj
    
  ni, nj = i+di, j+dj
  make_move(house, (ni, nj), mv)
  house[i][j], house[ni][nj] = house[ni][nj], house[i][j]
  return ni, nj
        

def part_two(input: list[str], verbose: bool) -> int:
  house, moves = define_params(input, verbose, p2=True)
  
  i, j = get_robot_coords(house)
  for move in moves:
    if can_make_move(house, (i, j), dir2move[move]):
      i, j = make_move(house, (i, j), dir2move[move])
  
    # print("\nMove:", move)
    # draw_matrix(house)
  
  return sum( 100 * i + j for i, row in enumerate(house) for j, val in enumerate(row) if val == "[")


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  for filename in sys.argv[1:]:
    print(f"\nFilename [ {filename} ]")
    input = read_file(filename)
    pr("Part One:", part_one(input, filename.startswith("test")))
    pr("Part Two:", part_two(input, filename.startswith("test")))
  