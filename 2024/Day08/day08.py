import sys
import pyperclip as cp
from collections import defaultdict


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)


Coord = tuple[int, int]
def calculate_antinodes(antennas: list[Coord], curr_ant: int, n: int, m: int, p2=False) -> set:  
  oi, oj = antennas[curr_ant]
  
  antinodes = set()
  for antenna, (i, j) in enumerate(antennas):
    if antenna == curr_ant:
      continue

    di, dj = (oi-i, oj-j) # get distance
    ni, nj = (oi+di, oj+dj) # antinode in curr node + distance
    
    if 0 <= ni < n and 0 <= nj < m:
      antinodes.add((ni, nj))
    
    if p2:
      antinodes.add((oi, oj)) 
      while 0 <= ni + di < n and 0 <= nj + dj < m:
        ni, nj = ni+di, nj+dj
        antinodes.add((ni, nj))
    
  return antinodes


VOID = '.'
def part_one(mapp: list[str], p2=False) -> int:
  n, m = len(mapp), len(mapp[0])
  
  antinodes = set()
  
  freq_coords = defaultdict(list)
  for antenna, row in enumerate(mapp):
    for j, freq in enumerate(row):
      if freq != VOID:
        freq_coords[freq].append((antenna, j))
  
  for freq, freq_antennas in freq_coords.items():
    for antenna, _ in enumerate(freq_antennas):
      antinodes |= calculate_antinodes(freq_antennas, antenna, n, m, p2)
  
  # for i, row in enumerate(mapp):
  #   for j, val in enumerate(row):
  #     d = val
  #     if d == '.' and (i, j) in antinodes:
  #       d = '#'
  #     print(d, end='')
  #   print()
    
  return len(antinodes)

def part_two(input: list[str]) -> int:
  return part_one(input, p2=True)

if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input = read_file(sys.argv[1])
  pr("Part One:", part_one(input))
  pr("Part Two:", part_two(input))
  