import sys
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)


operations = ["+", "*"]
def make_op(x: int, y: int, op: str) -> int:
  match op:
    case "+":
      return x + y
    case "*":
      return x * y
    case "||":
      lenght = 0
      
      yy = y
      while yy > 0:
        lenght += 1
        yy //= 10
        
      return x * (10 ** lenght) + y
    case _:
      print("o fac")
  
  return -1


def bt(e: int, n: int, nums: list[int], test:int, total: int) -> bool:
  if e == n:
    return total == test

  if e == 0:
    if bt(e+1, n, nums, test, nums[0]):
      return True
  
  else:
    for op in operations:
      res = make_op(total, nums[e], op)
      if res <= test:
        if bt(e+1, n, nums, test, res):
          return True
  
  return False


def part_one(input: list[str]) -> int:

  ans = 0
  for test, nums in map(lambda s: s.split(": "), input):
    nums = list(map(int, nums.split()))
    test = int(test)
    
    ans += test if bt(0, len(nums), nums, test, 0) else 0
    
  return ans
    

def part_two(input: list[str]) -> int:
  operations.append("||")
  return part_one(input)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  in1 = read_file(sys.argv[1])
  pr("Part One:", part_one(in1))
  pr("Part Two:", part_two(in1))
  