import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

Coord = tuple[int, int]

ROBOT, BOX, WALL, VOID = "@", "O", "#", "."

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
    print(moves)
  
  return house, moves


def get_robot_coords(house: list[list[str]]) -> Coord:
  for i, row in enumerate(house):
    for j, val in enumerate(row):
      if val == ROBOT:
        return i, j
  
  return -1, -1


def make_move(house: list[list[str]], start: Coord, mv: Coord) -> Coord:
  i, j = start
  
  if house[i][j] == WALL:
    return i, j
  
  di, dj = mv
  if house[i][j] == VOID:
    ni, nj = i+di, j+dj
    return ni, nj
  
  pi, pj = make_move(house, (i+di, j+dj), mv)
  ni, nj = pi-di, pj-dj
  
  house[i][j], house[ni][nj] = house[ni][nj], house[i][j]
  return ni, nj


def part_one(input: list[str], verbose: bool) -> int:
  house, moves = define_params(input, verbose)
  
  i, j = get_robot_coords(house)
  for move in moves:
    i, j = make_move(house, (i, j), dir2move[move])
    
    # print("\nMove:", move)
    # draw_matrix(house)
  
  return sum( 100 * i + j for i, row in enumerate(house) for j, val in enumerate(row) if val == BOX)


def part_two(input: list[str], verbose: bool) -> int:
  house, moves = define_params(input, verbose, p2=True)
  
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input = read_file(sys.argv[1])
  pr("Part One:", part_one(input, sys.argv[1].startswith("test")))
  pr("Part Two:", part_two(input, sys.argv[1].startswith("test")))
  