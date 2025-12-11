from collections import defaultdict
from functools import reduce
from tqdm import tqdm
from math import sqrt


OPT = 0 # 0 for test, 1 for input
INPUT_FILE, N_CONN = (("./test.txt", 10), ("./input.txt", 1000))[OPT] 


with open(INPUT_FILE) as fr:
  junction_boxes = fr.read().strip().split("\n")
  
junction_boxes = list(map(lambda x: tuple(map(int, x.split(","))), junction_boxes))
      
  
# =========== Part One =========== #

def calculate_euclidian_distance(box1, box2) -> int:
  x1, y1, z1 = box1
  x2, y2, z2 = box2
  return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2) + pow(z1-z2, 2))


circuits    = {box_id: {(x, y, z)} for box_id, (x, y, z) in enumerate(junction_boxes)}
box_circuit = {(x, y, z): box_id   for box_id, (x, y, z) in enumerate(junction_boxes)}


# calculate all distances just one time
distance: dict = {
  (box1, box2): calculate_euclidian_distance(box1, box2)
    for i, box1 in enumerate(junction_boxes) 
      for box2 in junction_boxes[i+1:]}
  
# for i, box1 in enumerate(junction_boxes): 
#   for box2 in junction_boxes[i+1:]:
#     distance[(box2, box1)] = distance[(box1, box2)]

circuits_id_idx = 1
sorted_distances = sorted([(dist, pair) for pair, dist in distance.items()])
    
with open("distances.txt", "w") as fw:
  for dist, (box1, box2) in sorted_distances:
    fw.write(f"{box1}, {box2}: {dist}\n")
    
for dist, (box1, box2) in sorted_distances[:N_CONN]:
  circuit_id_box1, circuit_id_box2 = box_circuit[box1], box_circuit[box2]
   
  if circuit_id_box1 != circuit_id_box2:
    circuits[circuit_id_box1] |= circuits[circuit_id_box2]
    
    for box in circuits[circuit_id_box2]:
      box_circuit[box] = circuit_id_box1
    
    del circuits[circuit_id_box2]

# for key, val in circuits.items():
#   print(f"{key}: {val} {len(val)}")
#   print()

print(f"Part One: {reduce(lambda x, y: x*y, sorted(list(map(lambda x: len(x), circuits.values())), reverse=True)[:3])}")


# =========== Part Two =========== #

circuits = {0: {(x, y, z) for x, y, z in junction_boxes}}
box_circuit = {(x, y, z): 0 for x, y, z in junction_boxes}

i = 0
while len(circuits) > 1:
  dist, (box1, box2) = sorted_distances[i]
  
  if box1 in [(216,146,977), (117,168,530)] and box2 in [(216,146,977), (117,168,530)]:
    print(circuits)
  
  circuit_id_box1, circuit_id_box2 = box_circuit[box1], box_circuit[box2]
  
  if circuit_id_box1 == circuit_id_box2 and circuit_id_box1 != 0:
    i += 1
    continue
  
  if circuit_id_box1 == 0 and circuit_id_box2 == 0:
    circuits[0].remove(box1)
    circuits[0].remove(box2)
    
    circuits[circuits_id_idx] = {box1, box2}
    box_circuit[box1] = circuits_id_idx
    box_circuit[box2] = circuits_id_idx
    
    circuits_id_idx += 1
  
  elif circuit_id_box1 != circuit_id_box2 and 0 in [circuit_id_box1, circuit_id_box2]:
    circuit_id_org, circuit_id_dst = (circuit_id_box1, circuit_id_box2) if circuit_id_box1 == 0 else (circuit_id_box2, circuit_id_box1)
    box_org = box1 if circuit_id_box1 == 0 else box2
    
    circuits[circuit_id_org].remove(box_org)
    circuits[circuit_id_dst].add(box_org)
    
    box_circuit[box_org] = circuit_id_dst
  
  else:
    circuits[circuit_id_box1] |= circuits[circuit_id_box2]
    
    for box in circuits[circuit_id_box2]:
      box_circuit[box] = circuit_id_box1
    
    del circuits[circuit_id_box2]
  if box1 in [(216,146,977), (117,168,530)] and box2 in [(216,146,977), (117,168,530)]:
    print(circuits)
  i += 1
  

print(circuits)
print(box1, box2)
print(f"Part Two: {box1[0] * box2[0]}")
