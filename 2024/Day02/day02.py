

def read_file(filename: str) -> list[str]:
  with open(filename, "r") as rfile:
    return rfile.readlines()
  

def is_safe(row: list[int]) -> bool:
  n = len(row)
  
  if n == 1:
    return True
  
  asc = row[0] < row[1]
  for i in range(1, n):
    if row[i] == row[i-1]:
      return False
    
    if row[i] < row[i-1]: # desc
      if asc:
        return False
    
    elif row[i-1] < row[i]: # asc
      if not asc:
        return False
    
    if abs(row[i] - row[i-1]) > 3:
      return False
  
  return True

  
def part_one(input: list[str]) -> int:
  m = list(map(lambda x: list(map(int, x.split())), input))
  return sum(is_safe(row) for row in m)


def part_two(input: list[str]) -> int:
  m = list(map(lambda x: list(map(int, x.split())), input))
  
  cnt = 0
  for row in m:
    # if original row is safe, go next
    if is_safe(row):
      cnt += 1
      continue
    
    # remove 1 to 1 each element and try if it is save now
    cnt += any(is_safe(row[:i] + row[i+1:]) for i in range(len(row))) 
    
  return cnt


if __name__ == "__main__":
  test = read_file("./test.in")
  
  sol1 = part_one(test)
  assert sol1 == 2, f"Expected 2, but got {sol1}."
  
  in1 = read_file("./in1.in")
  print(f"Part One: {part_one(in1)}")
  
  sol2 = part_two(test)
  assert sol2 == 5, f"Expected 5, but got {sol2}."
  
  print(f"Part Two: {part_two(in1)}")
  