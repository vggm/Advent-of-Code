from math import ceil

POSSIBLE_MOVES = ((-1, 0), (0, -1), (0, 1), (1, 0))
moves = {
  '|': ((1, 0), (-1, 0)),
  '-': ((0, 1), (0, -1)),
  'L': ((-1, 0), (0, 1)),
  'J': ((-1, 0), (0, -1)),
  '7': ((0, -1), (1, 0)),
  'F': ((1, 0), (0, 1)),
}


maze: list[str]


def get_maze(filename: str) -> list[str]:
  return open(filename).read().strip().split('\n')


def find_S() -> (int, int):
  for ii, row in enumerate(maze):
    for jj, c in enumerate(row):
      if c == 'S':
        return ii, jj

  return -1, -1


def call_part_func(func, part: str) -> None:
  si, sj = find_S()

  found = False
  for movement in POSSIBLE_MOVES:
    ri, rj = si + movement[0], sj + movement[1]
    m_symbol = maze[ri][rj]
    if movement == (1, 0) and m_symbol in ['L', 'J', '|']:
      found = True
    elif movement == (-1, 0) and m_symbol in ['F', '7', '|']:
      found = True
    elif movement == (0, 1) and m_symbol in ['7', 'J', '-']:
      found = True
    elif movement == (0, -1) and m_symbol in ['L', 'F', '-']:
      found = True

    if found:
      ans = func((ri, rj), (si, sj))
      print(f'{part} part: {ceil(ans / 2)}')
      break


def part_one(*args) -> int:
  i, j = args[0]

  curr = maze[i][j]
  last = args[1]

  step = 0
  while curr != 'S':

    temp = i, j
    next_move = moves[curr]

    if (i + next_move[0][0], j + next_move[0][1]) != last:
      i, j = i + next_move[0][0], j + next_move[0][1]
    else:
      i, j = i + next_move[1][0], j + next_move[1][1]

    last = temp
    curr = maze[i][j]

    step += 1

  return step


def maze_to_set() -> set:
  set_of_coords = set()
  for i, row in enumerate(maze):
    for j, _ in enumerate(row):
      set_of_coords.add((i, j))
  return set_of_coords


def explore_and_remove(start: tuple[int, int], not_wall: set) -> None:
  i, j = start
  if start not in not_wall:
    return

  not_wall.remove(start)

  for ii, jj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    if 0 <= i + ii < len(maze) and 0 <= j + jj < len(maze[0]):
      explore_and_remove((i + ii, j + jj), not_wall)


def part_two(*args) -> int:
  i, j = args[0]

  curr = maze[i][j]
  last = args[1]

  wall: set = {last, (i, j)}

  while curr != 'S':

    temp = i, j
    next_move = moves[curr]

    if (i + next_move[0][0], j + next_move[0][1]) != last:
      i, j = i + next_move[0][0], j + next_move[0][1]
    else:
      i, j = i + next_move[1][0], j + next_move[1][1]

    last = temp
    curr = maze[i][j]

    wall.add(last)

  inside = set()
  cont = 0
  for i, row in enumerate(maze):
    odd = False
    for j, v in enumerate(row):
      if odd:
        inside.add((i, j))
        cont += 1

      if v in '|JL':
        odd = not odd

  for i, row in enumerate(maze):
    for j, v in enumerate(row):
      if (i, j) in wall:
        print('#', end=' ')
      elif (i, j) in inside:
        print('I', end=' ')
      else:
        print('.', end=' ')
    print()

  return cont


if __name__ == '__main__':
  maze = get_maze('test3.txt')
  call_part_func(part_one, 'First')
  # call_part_func(part_two, 'Second')
