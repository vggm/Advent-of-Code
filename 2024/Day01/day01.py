from heapq import heappop, heappush
from typing import Counter


def part_one(input: list[str]) -> int:
  
  left, right = [], []
  for l, r in list(map(str.split, input)):
    heappush(right, int(r))
    heappush(left, int(l))
  
  total_diff = 0  
  while left and right:
    l, r = heappop(left), heappop(right)
    total_diff += abs(l - r)
  
  return total_diff


def part_two(input: list[str]) -> int:
  
  left, right = [], []
  for l, r in list(map(str.split, input)):
    right.append(int(r))
    left.append(int(l))
  
  freq = Counter(right)
  return sum(l*freq[l] for l in left)


def read_file(filename: str) -> list[str]:
  with open(filename, "r") as rfile:
    return rfile.readlines()  


if __name__ == "__main__":
  test = read_file("./2024/day01/test.txt")
  
  sol = part_one(test)
  assert sol == 11, f"Expected 11, but got {sol}."
  
  input1 = read_file("./2024/day01/input1.txt")
  print(f"Part One: {part_one(input1)}")
  
  sol = part_two(test)
  assert sol == 31, f"Expected 31, but got {sol}."
  
  print(f"Part Two: {part_two(input1)}")
  