from collections import defaultdict
from math import sqrt


OPT = 1 # 0 for test, 1 for input
INPUT_FILE, N_CONN = (("./test.txt", 10), ("./input.txt", 1000))[OPT] 


with open(INPUT_FILE) as fr:
  junction_boxes = fr.read().strip().split("\n")
  
junction_boxes = list(map(lambda x: list(map(int, x.split(","))), junction_boxes))
      
  
# =========== Part One =========== #
  
def distance(box1, box2) -> int:
  x1, y1, z1 = box1
  x2, y2, z2 = box2
  return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2) + pow(z1-z2, 2))


circuits = {0: {(x, y, z) for x, y, z in junction_boxes}}
box2circuit = {(x, y, z): 0 for x, y, z in junction_boxes}


for _ in range(N_CONN):
  for i, box1 in enumerate(junction_boxes):
    for box2 in junction_boxes[i+1:]:
      distance(box1, box2)


# =========== Part Two =========== #


