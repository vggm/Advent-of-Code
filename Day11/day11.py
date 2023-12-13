
size_to_expand = 2
space_map: list[str]

def read_galaxies(filename: str) -> list[str]:
  return open(filename).read().strip().split('\n')


def get_expand_edges() -> (list[int], list[int]):
  expand_i = [i for i, row in enumerate(space_map) 
                if row.count('#') == 0]
  
  trunc_space = list(zip(*space_map))
  expand_j = [j for j, row in enumerate(trunc_space)
                if ''.join(row).count('#') == 0]

  return expand_i, expand_j


def find_galaxies() -> dict:
  galaxies = {}
  for i, row in enumerate(space_map):
    for j, v in enumerate(row):
      if v == '#':
        galaxies[len(galaxies)+1] = (i, j)
  return galaxies


def calculate_distance(org: tuple[int, int], dst: tuple[int, int], i_edges: list[int], j_edges: list[int]) -> int:
  (oi, oj), (di, dj) = org, dst
  
  cnt = 0
  start, end = min(oi, di), max(oi, di)
  for i in range(start, end):
    if i in i_edges:
      cnt += 1
  
  start, end = min(oj, dj), max(oj, dj)
  for j in range(start, end):
    if j in j_edges:
      cnt += 1
  
  return abs(oi-di) + abs(oj-dj) + cnt * (size_to_expand - 1)


def part_one(galaxies: dict, edges_i: list[int], edges_j: list[int]) -> int:
  galaxy_dist_calculated = set()
  total_distance = 0
  for galaxy_a, coords_a in galaxies.items():
    for galaxy_b, coords_b in galaxies.items():
      if galaxy_a != galaxy_b:
        if (galaxy_b, galaxy_a) not in galaxy_dist_calculated:
          galaxy_dist_calculated.add((galaxy_a, galaxy_b))
          distance = calculate_distance(coords_a, coords_b, edges_i, edges_j)
          total_distance += distance
  return total_distance


if __name__ == '__main__':
  space_map = read_galaxies('input.txt')
  exp_i, exp_j = get_expand_edges()
  galaxies_coords = find_galaxies()
  ans = part_one(galaxies_coords, exp_i, exp_j)
  print(f'Part one: {ans}')
  size_to_expand = 1000000
  ans = part_one(galaxies_coords, exp_i, exp_j)
  print(f'Part two: {ans}')
  
