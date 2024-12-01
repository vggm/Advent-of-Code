
VOID = '.'
ROCK = 'O'
WALL = '#'

CYCLES = 1000000000


def print_board(board: tuple[str]) -> None:
  for row in board:
    print(row)
  print()


def get_board(filename: str) -> tuple[tuple[str]]:
  return tuple(row for row in open(filename).read().strip().split('\n'))


def calculate_load(board: tuple[str]) -> int:
  return sum(row.count(ROCK) * (len(board) - index) 
             for index, row in enumerate(board))
  

def slide_rocks(board: tuple[str]) -> tuple[str]:
  tboard = list(map(''.join, zip(*board)))
  new_board = []
  
  for row in tboard:
    new_rows = []
    for group in row.split(WALL):
      new_rows.append(''.join(sorted(group, reverse=True)))
    new_board.append(WALL.join(new_rows))
    
  return tuple(map(''.join, zip(*new_board)))


def do_cycle(board: tuple[str]) -> tuple[str]:
  for _ in range(4):
    board = slide_rocks(board)
    # print_board(board)
    board = tuple(''.join(row[::-1]) for row in zip(*board))
  # print_board(board)
  return board


def part_one(board: tuple[int]) -> int:
  return calculate_load(slide_rocks(board))


def part_two(board: tuple[int]) -> int:  
  
  visited = {board}
  visited_list = [board]
  
  curr_cycle = board
  i, found = 0, False
  while i < CYCLES and not found:
    curr_cycle = do_cycle(curr_cycle)
    
    if curr_cycle in visited:
      found = True
    else:
      visited.add(curr_cycle)
      visited_list.append(curr_cycle)
      i += 1
  
  first_cycle_index = visited_list.index(curr_cycle)
  final_board = visited_list[
    (CYCLES - first_cycle_index) % (i + 1 - first_cycle_index)
    + first_cycle_index
  ]
  
  return calculate_load(final_board)


if __name__ == '__main__':
  started_board = get_board('./input.txt')
  print(f'Part one: {part_one(started_board)}')
  print(f'Part two: {part_two(started_board)}')
