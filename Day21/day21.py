

MOVE = 'O'
ROCK = '#'
POSSIBLE_MOVES = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def print_garden(garden: list[str]) -> None:
  for row in garden:
    print(row)
  print('-' * len(garden[0]))


def get_map_pos(filename: str) -> (list[str], tuple[int, int]):
  garden = []
  started_position = (0, 0)
  for i, row in enumerate(open(filename).read().strip().split('\n')):
    garden.append(row)
    if 'S' in row:
      started_position = (i, row.find('S'))
  return garden, started_position
  
  
def replace_position(garden: list[str], pos: tuple[int], replace: str) -> None:
  i, j = pos
  garden[i] = garden[i][:j] + replace + garden[i][j+1:]
  
  
def set_possible_moves(garden: list[str], pos: tuple[int, int]) -> None:
  i, j = pos
  replace_position(garden, pos, '.')
  for move in POSSIBLE_MOVES:
    y, x = move
    ni, nj = i+y, j+x
    if 0 <= ni < len(garden) and 0 <= nj < len(garden[0])\
      and garden[ni][nj] not in [ROCK, MOVE]:
      replace_position(garden, (ni, nj), MOVE)
      
      
def count_moves(garden: list[str]) -> int:
  return sum(row.count(MOVE) for row in garden)
    

def part_one(garden: list[str], started_position: tuple[int, int], max_steps: int) -> int:
  
  if max_steps == 0:
    return 0
  
  set_possible_moves(garden, started_position)
  
  step = 1
  while step < max_steps:
    curr_garden = garden[:]
    for gi, row in enumerate(garden):
      for gj, c in enumerate(row):
        if c == MOVE:
          set_possible_moves(curr_garden, (gi, gj))
    
    garden = curr_garden[:]
    # print_garden(garden)
        
    step += 1
  
  return count_moves(garden)


def set_moves(garden: list[str], pos: tuple[int, int], moves: set) -> None:
  i, j = pos
  for move in POSSIBLE_MOVES:
    y, x = move
    ni, nj = i+y, j+x
    if garden[ni % len(garden)][nj % len(garden[0])] != ROCK\
      and (ni, nj) not in moves:
      moves.add((ni, nj))


def part_one_w_set(garden: list[str], started_position: tuple[int, int], max_steps: int) -> int:
  
  possible_moves = set()
  set_moves(garden, started_position, possible_moves)
  
  step = 1  
  while step < max_steps:
    
    curr_possible_moves = set()
    for pos in possible_moves:
      set_moves(garden, pos, curr_possible_moves)      
    
    possible_moves = curr_possible_moves
    step += 1
  
  return len(possible_moves)
  

def main() -> None:
  G, S = get_map_pos('./input.txt')
  print(f'Part One: {part_one(G, S, 64)}') 


if __name__ == "__main__":
  main()
# end main