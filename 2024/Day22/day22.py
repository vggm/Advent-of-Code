import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 
 
PRUNE_NUM = 16777216
 

def part_one(secrets: list[str]) -> int:
  
  total_sum = 0
  for secret in map(int, secrets):
    org_secret = secret
    for _ in range(2_000):
      old_secret = secret
      
      secret *= 64
      secret ^= old_secret
      secret %= PRUNE_NUM
      
      old_secret = secret
      
      secret //= 32
      secret ^= old_secret
      secret %= PRUNE_NUM
      
      old_secret = secret
      
      secret *= 2048
      secret ^= old_secret
      secret %= PRUNE_NUM
      
    # print(org_secret, ":", secret)
    total_sum += secret
  
  return total_sum


def part_two(secrets: list[str]) -> int:
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  # pr("Part Two:", part_two(file_input))
  