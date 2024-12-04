import re


def read_file(filename: str) -> list[str]:
  with open(filename, "r") as rfile:
    return rfile.readlines()


def part_one(input: list[str]) -> int:
  total = 0
  for row in input:
    matches = re.findall(r"mul\((\d+),(\d+)\)", row)
    total += sum(int(m1)*int(m2) for m1, m2 in matches)

  return total


def part_two(input: list[str]) -> int:
  total = 0
  enable = True
  for row in input:
    
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", row)
    
    for x, y, op in matches:
      if op:
        enable = (op == "do()")
        
      elif enable:
        total += int(x) * int(y)
        
  return total


if __name__ == '__main__':
  test = read_file("./test1.in")
  
  sol = part_one(test)
  assert sol == 161, f"Expected 161, but got {sol}."
  
  in1 = read_file("./in1.in")
  print(f"Part One: {part_one(in1)}")
  
  test = read_file("./test2.in")
  
  sol = part_two(test)
  assert sol == 48, f"Expected 48, but got {sol}."
  
  print(f"Part Two: {part_two(in1)}")
  