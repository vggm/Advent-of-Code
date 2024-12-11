import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

def part_one(input: list[str]) -> int:
  return -1


def part_two(input: list[str]) -> int:
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input = read_file(sys.argv[1])
  pr("Part One:", part_one(input))
  # pr("Part Two:", part_two(input))
  