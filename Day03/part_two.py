
NOT_A_SYMBOL = [
  '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'
]


class EngineSchematic:
  def __init__(self):
    self.map: list[str] = []
    self.gear_symbols: list[tuple[int, int]] = []
    self.cols = 0
    self.rows = 0
    self.cells = 0

  def __getitem__(self, item):
    return self.map[item]


def read_file(filename: str) -> EngineSchematic:
  es = EngineSchematic()
  with open(filename) as file:
    row = file.readline().removesuffix('\n')
    while row != '':
      es.map.append(row)

      if row.count('*') > 0:
        for i, c in enumerate(row):
          if c == '*':
            es.gear_symbols.append((es.rows, i))

      es.rows += 1
      row = file.readline().removesuffix('\n')

    es.cols = len(es[0])
    es.cells = es.rows * es.cols
  return es


def expand_number(coords: tuple[int, int], es: EngineSchematic) -> int:
  i, j = coords
  number = es[i][j]

  start, end = j, j
  first, last = False, False
  while not (first and last):
    if start - 1 >= 0 and es[i][start - 1].isdigit():
      number = es[i][start-1] + number
      start -= 1
    else:
      first = True

    if end + 1 < es.cols and es[i][end + 1].isdigit():
      number += es[i][end+1]
      end += 1
    else:
      last = True

  return int(number)


def find_number(coords: tuple[int, int], es: EngineSchematic) -> list[int]:
  i, j = coords
  numbers = set()

  for ii, jj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    if (0 <= i + ii < es.rows) and (0 <= j + jj < es.cols):
      if es[i + ii][j + jj].isdigit():
        number_found = expand_number((i+ii, j+jj), es)
        numbers.add(int(number_found))

  return list(numbers)


def search_gear(es: EngineSchematic) -> int:

  total_sum = 0

  for coords in es.gear_symbols:
    gear = find_number(coords, es)
    if len(gear) == 2:
      total_sum += gear[0] * gear[1]

  return total_sum


if __name__ == '__main__':
  engine_schematic = read_file('input.txt')
  ans = search_gear(engine_schematic)
  print('Total sum:', ans)
