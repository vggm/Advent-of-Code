
space_map: list[str]

def read_galaxies(filename: str) -> list[str]:
  return open(filename).read().strip().split('\n')


def expand_space() -> None:
  expand_i = [i for i, row in enumerate(space_map) 
                if row.count('#') == 0]
  
  trunc_space = list(zip(*space_map))
  expand_j = [j for j, row in enumerate(trunc_space)
                if ''.join(row).count('#') == 0]
  
  cnt = 0
  for i in expand_i:
    space_map.insert(i+cnt, '.' * (len(space_map)-cnt))
    cnt += 1
    
  for i in range(len(space_map)):
    cnt = 0
    for j in expand_j:
      space_map[i] = space_map[i][:j+cnt] + '.' + space_map[i][j+cnt:]
      cnt += 1  


def find_galaxies() -> dict:
  galaxies = {}
  for i, row in enumerate(space_map):
    for j, v in enumerate(row):
      if v == '#':
        galaxies[len(galaxies)+1] = (i, j)
  return galaxies


def calculate_distance(org: tuple[int, int], dst: tuple[int, int]) -> int:
  (oi, oj), (di, dj) = org, dst
  return abs(oi-di) + abs(oj-dj)


def part_one(galaxies: dict) -> int:
  galaxy_dist_calculated = set()
  total_distance = 0
  for galaxy_a, coords_a in galaxies.items():
    for galaxy_b, coords_b in galaxies.items():
      if galaxy_a != galaxy_b:
        if (galaxy_b, galaxy_a) not in galaxy_dist_calculated:
          galaxy_dist_calculated.add((galaxy_a, galaxy_b))
          distance = calculate_distance(coords_a, coords_b)
          total_distance += distance
  return total_distance


if __name__ == '__main__':
  space_map = read_galaxies('input.txt')
  expand_space()
  galaxies_coords = find_galaxies()
  ans = part_one(galaxies_coords)
  print(f'Part one: {ans}')
  
