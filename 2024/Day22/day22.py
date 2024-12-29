from collections import deque
from functools import cache
import pyperclip as cp
import sys

sys.setrecursionlimit(2_004)

def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 
 
PRUNE_NUM = 16777216
def generate_secret_2000(secret: int) -> int:
  for _ in range(2_000):
      old_secret = secret
      
      secret *= 64
      secret ^= old_secret # mix
      secret %= PRUNE_NUM  # prune
      
      old_secret = secret
      
      secret //= 32
      secret ^= old_secret # mix
      secret %= PRUNE_NUM  # prune
      
      old_secret = secret
      
      secret *= 2048
      secret ^= old_secret # mix
      secret %= PRUNE_NUM  # prune
  
  return secret


@cache
def generate_n_secret(n:int, org: int) -> int:
  if n == 0:
    return org
  
  new_secret = generate_n_secret(n-1, org)
  old_secret = new_secret
  
  new_secret *= 64
  new_secret ^= old_secret # mix
  new_secret %= PRUNE_NUM  # prune
  
  old_secret = new_secret
      
  new_secret //= 32
  new_secret ^= old_secret # mix
  new_secret %= PRUNE_NUM  # prune
  
  old_secret = new_secret
  
  new_secret *= 2048
  new_secret ^= old_secret # mix
  new_secret %= PRUNE_NUM  # prune
  
  return new_secret


def part_one(secrets: list[str]) -> int:
  return sum(map(lambda x: generate_n_secret(2_000, int(x)), secrets))


def part_two(secrets: list[str]) -> int:
  
  paths: list[dict[tuple, int]] = []
  for secret in map(int, secrets):
    lst = secret % 10
    path: dict[tuple, int] = {}
    
    # calculate first 4 tuples 
    window = deque([])
    for i in range(1, 5):
      n = generate_n_secret(i, secret)
      window.append(n % 10 - lst)
      lst = n % 10
    path[tuple(window)] = n % 10
    
    # calculte for the rest of the 2000 secrets generated
    for i in range(5, 2_001):
      n = generate_n_secret(i, secret)

      # update sliding window
      window.popleft()
      window.append(n % 10 - lst)
      
      if tuple(window) not in path:
        path[tuple(window)] = n % 10
      
      lst = n % 10
    
    paths.append(path)
    
  # get all the slidings windows saved
  tpls = set()
  for path in paths:
    tpls |= set(path.keys())
  
  ans = 0
  for tpl in tpls:
    # check every slice in all paths
    ans = max(ans, sum(path[tpl] for path in paths\
                    if tpl in path))
  
  return ans


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  