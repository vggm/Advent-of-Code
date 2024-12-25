import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 
 
def separe(locks_key: list[list[str]]) -> tuple[list[list[str]], list[list[str]]]:
  locks, keys = [], []
  for lock_or_key in locks_key:
    if lock_or_key[0][0] == "#":
      locks.append(lock_or_key)
    else:
      keys.append(lock_or_key)
  
  return locks, keys


def to_vector(lock_key: list[str]) -> list[int]:
  vector = []
  for column in zip(*lock_key):
    vector.append(column.count("#") - 1)
    
  return vector


def part_one(locks_keys: list[str]) -> int:
  locks_keys = list(map(lambda x: x.split("\n"), locks_keys))
  locks, keys = separe(locks_keys)
  
  locks = list(map(to_vector, locks))
  keys = list(map(to_vector, keys))
  
  fits = 0
  for lock in locks:
    for key in keys:
      for x, y in zip(lock, key):
        if (x + y) > 5:
          break
      else:
        fits += 1
        
  return fits


def part_two(file_input: list[str]) -> int:
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  # pr("Part Two:", part_two(file_input))
  