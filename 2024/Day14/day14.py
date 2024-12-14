import sys
import cv2 as cv  
import pyperclip as cp
import numpy as np


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)


TEST_DIMENSION, INPUT_DIMENSION = (7, 11), (103, 101)


def extract_params(line: str) -> tuple[int, int, int, int]:
  pos, speed = line.split(" ")
  return list(map(int, pos[2:].split(","))), list(map(int, speed[2:].split(",")))
 

def part_one(robots: list[str], n: int, m: int, seconds=100) -> int:
  mapp = [[0 for _ in range(m)] for _ in range(n)]
  
  for (j, i), (sj, si) in map(extract_params, robots):
    for _ in range(seconds):
      i, j = (i+si) % n, (j+sj) % m
    mapp[i][j] += 1
  
  mi, mj = n // 2, m // 2
  
  q1 = sum(mapp[i][j] for i in range(mi) for j in range(mj))
  q2 = sum(mapp[i][j] for i in range(mi) for j in range(mj+1, m))
  q3 = sum(mapp[i][j] for i in range(mi+1, n) for j in range(mj))
  q4 = sum(mapp[i][j] for i in range(mi+1, n) for j in range(mj+1, m))
  
  return q1 * q2 * q3 * q4


def part_two(robots: list[str], n: int, m: int, seconds=100):
  mapp = [[0 for _ in range(m)] for _ in range(n)]
  
  params: list[list[int]] = []
  for (j, i), (sj, si) in map(extract_params, robots):
    mapp[i][j] += 1
    params.append([i, j, si, sj])
    
  # for row in mapp:
  #   for val in row:
  #     print(" " if not val else "#", end='')
  #   print()
  # print("Second: 0")
  
  for second in range(1, seconds+1):
    for index, (i, j, si, sj) in enumerate(params):
      mapp[i][j] -= 1
      i, j = (i+si) % n, (j+sj) % m
      mapp[i][j] += 1
      params[index] = [i, j, si, sj]
    
    bin_matrix = [[0 if not mapp[i][j] else 255 for j in range(m)] for i in range(n)]
    cv.imwrite("./figures/second_%d.png" % second, np.array(bin_matrix))
    
    # for row in mapp:
    #   for val in row:
    #     print(" " if not val else "#", end='')
    #   print()
    # print(f"Second: {second}")


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input_file = read_file(sys.argv[1])
  n, m = TEST_DIMENSION if sys.argv[1].startswith("test") else INPUT_DIMENSION
  
  pr("Part One:", part_one(input_file, n, m, seconds=100))
  pr("Part Two:", part_two(input_file, n, m, seconds=8000))
  