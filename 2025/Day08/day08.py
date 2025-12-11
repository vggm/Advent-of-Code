from functools import reduce
from math import sqrt


OPT = 1 # 0 for test, 1 for input
INPUT_FILE, N_CONN = (("./test.txt", 10), ("./input.txt", 1000))[OPT] 


with open(INPUT_FILE) as fr:
  junction_boxes = fr.read().strip().split("\n")
  
junction_boxes = list(map(lambda x: tuple(map(int, x.split(","))), junction_boxes))
      
  
# =========== Part One =========== #

def euclidian_distance(box1, box2) -> int:
  x1, y1, z1 = box1
  x2, y2, z2 = box2
  return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2) + pow(z1-z2, 2))


circuits    = {circ_id: {(x, y, z)} for circ_id, (x, y, z) in enumerate(junction_boxes)}
circuit_id  = {(x, y, z): circ_id   for circ_id, (x, y, z) in enumerate(junction_boxes)}


# calculate all distances just one time
distance: dict = {
  (box1, box2): euclidian_distance(box1, box2)
    for i, box1 in enumerate(junction_boxes) 
      for box2 in junction_boxes[i+1:]}

sorted_distances = sorted([(dist, pair) for pair, dist in distance.items()])
    
    
for dist, (box1, box2) in sorted_distances[:N_CONN]:
  circuit_id_box1, circuit_id_box2 = circuit_id[box1], circuit_id[box2]
   
  if circuit_id_box1 != circuit_id_box2:
    circuits[circuit_id_box1] |= circuits[circuit_id_box2] # join circuits
    
    for box in circuits[circuit_id_box2]:
      circuit_id[box] = circuit_id_box1 # update value
    
    del circuits[circuit_id_box2]


circuits_len = list(map(lambda x: len(x), circuits.values()))
circuits_len.sort(reverse=True) # desc order

print(f"Part One: {reduce(lambda x, y: x*y, circuits_len[:3])}")


# =========== Part Two =========== #

circuits    = {box_id: {(x, y, z)} for box_id, (x, y, z) in enumerate(junction_boxes)}
circuit_id  = {(x, y, z): box_id   for box_id, (x, y, z) in enumerate(junction_boxes)}


for dist, (box1, box2) in sorted_distances:
  
  circuit_id_box1, circuit_id_box2 = circuit_id[box1], circuit_id[box2]
   
  if circuit_id_box1 != circuit_id_box2:
    circuits[circuit_id_box1] |= circuits[circuit_id_box2]
    
    for box in circuits[circuit_id_box2]:
      circuit_id[box] = circuit_id_box1
    
    del circuits[circuit_id_box2]
  
    if len(circuits) == 1:
      break
  
  
print(f"Part Two: {box1[0] * box2[0]}")
print("Last boxes:", box1, box2)
