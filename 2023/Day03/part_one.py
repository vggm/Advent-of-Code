
NOT_A_SYMBOL = [
  '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'
]


class EngineSchematic:
  def __init__(self):
    self.map: list[str] = []
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
      es.rows += 1
      row = file.readline().removesuffix('\n')

    es.cols = len(es[0])
    es.cells = es.rows * es.cols
  return es


def calculate_coord(k: int, cols: int) -> (int, int):
  return k // cols, k % cols


def has_symbols(start: tuple[int, int], end: tuple[int, int], es: EngineSchematic) -> bool:
  i = start[0]
  for j in range(start[1], end[1] + 1):
    if (i, j) == start:
      for y, x in [(-1, -1), (0, -1), (1, -1)]:
        if (0 <= i + y < es.rows) and (0 <= j + x < es.cols):
          if es[i + y][j + x] not in NOT_A_SYMBOL:
            return True

    if (i, j) == end:
      for y, x in [(-1, 1), (0, 1), (1, 1)]:
        if (0 <= i + y < es.rows) and (0 <= j + x < es.cols):
          if es[i + y][j + x] not in NOT_A_SYMBOL:
            return True

    for y in [1, -1]:
      if 0 <= i + y < es.rows:
        if es[i + y][j] not in NOT_A_SYMBOL:
          return True

  return False


def search_part_numbers(es: EngineSchematic) -> int:

  temp = ''
  total_sum = 0
  start, end = (-1, -1), (-1, -1)
  for k in range(es.cells):
    i, j = calculate_coord(k, es.rows)
    cell_value = es[i][j]

    if not cell_value.isdigit():  # not digit
      continue

    else:  # is digit
      if not temp:
        start = (i, j)
      temp += cell_value

      if (j == es.cols - 1) or not es[i][j+1].isdigit():  # last digit
        end = (i, j)
        if has_symbols(start, end, es):
          total_sum += int(temp)

        temp = ''

  return total_sum


if __name__ == '__main__':
  engine_schematic = read_file('input.txt')
  ans = search_part_numbers(engine_schematic)
  print('Total sum:', ans)
