
class Param:
  def __init__(self, m=0, mx=0, d=0):
    self.min = m
    self.max = mx
    self.diff = d


class SeedTransform:
  def __init__(self):
    self.params = []
    self.min = float('inf')
    self.max = -1

  def clear(self):
    self.params = []
    self.min = float('inf')
    self.max = -1

  def add_param(self, org: int, dst: int, size: int) -> None:
    param = Param(
      org,              # min
      org + size - 1,   # max
      org - dst         # diff
    )

    if param.min < self.min:
      self.min = param.min

    if param.max > self.max:
      self.max = param.max

    self.params.append(param)

  def transform(self, org: int) -> int:
    if org > self.max or org < self.min:
      return org

    for param in self.params:
      if org > param.max or org < param.min:
        continue

      return org - param.diff

    return org

  def transform_all(self, org_list: list[int]) -> None:
    for i, org in enumerate(org_list):
      org_list[i] = self.transform(org)


def read_file(filename: str) -> list[int]:
  seed_transform = SeedTransform()
  with open(filename) as file:
    seeds = file.readline().split(':')[1].split()
    values = [int(x) for x in seeds]
    # print(f'seed: {values}')
    file.readline()  # blank space

    last = ''
    param = file.readline()
    while param != '':

      if param == '\n':
        seed_transform.transform_all(values)
        # print(f'{last}: {values}')
        seed_transform.clear()

      elif param.count('-') == 0:
        dst, org, size = param.split()
        seed_transform.add_param(int(org), int(dst), int(size))

      else:
        last = param.split('-')[2].split()[0]

      param = file.readline()

  seed_transform.transform_all(values)
  # print(f'{last}: {values}')

  return values


if __name__ == '__main__':
  locations = read_file('input.txt')
  # print(locations)
  print('Min:', min(locations))
