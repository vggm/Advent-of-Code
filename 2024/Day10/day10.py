import sys
import pyperclip as cp


def read_file(filename: str) -> str:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)


def part_one(mapp: list[str]) -> int:
  n, m = len(mapp), len(mapp[0])
  mapp = list(map(lambda row: list(map(int, list(row))), mapp))
  # print(mapp)
  
  def bt(i: int, j: int, seen: set) -> int:
    seen.add((i, j))
    
    if mapp[i][j] == 9:
      return 1
    
    return sum(bt(ni, nj, seen) 
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] 
                  if 0 <= ni < n and 0 <= nj < m        # inside the map
                    and (ni, nj) not in seen            # not seen
                    and mapp[ni][nj] == mapp[i][j] + 1) # the next val is 1 above curr val
  
  return sum(bt(i, j, set())
              for i, row in enumerate(mapp)
                for j, val in enumerate(row)
                  if val == 0)


def part_two(mapp: list[str]) -> int:
  n, m = len(mapp), len(mapp[0])
  mapp = list(map(lambda row: list(map(int, list(row))), mapp))
  # print(mapp)
  
  # same as p1 but not saving the positions visited
  def bt(i: int, j: int) -> int:
    
    if mapp[i][j] == 9:
      return 1
    
    return sum(bt(ni, nj) 
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] 
                  if 0 <= ni < n and 0 <= nj < m        # inside the map
                    and mapp[ni][nj] == mapp[i][j] + 1) # the next val is 1 above curr val
  
  return sum(bt(i, j)
              for i, row in enumerate(mapp)
                for j, val in enumerate(row)
                  if val == 0)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input = read_file(sys.argv[1])
  pr("Part One:", part_one(input))
  pr("Part Two:", part_two(input))
  