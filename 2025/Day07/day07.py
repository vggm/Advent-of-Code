
from collections import deque


with open("./input.txt") as fr:
  lines = fr.read().strip().split("\n")

SPLIT_SYMBOL = "^"
START_SYMBOL = "S"
ROWS, COLS = len(lines), len(lines[0])

splitters = []
for i, row in enumerate(lines):
  for j, val in enumerate(row):
    if val == SPLIT_SYMBOL:
      splitters.append((i, j))
      
      
start_col = lines[0].find(START_SYMBOL)
      
  
# =========== Part One =========== #

#########################################
## First Approach: Following the beams ##
#########################################

# find the first split
active_splitter = set()
for i in range(1, ROWS):
  if lines[i][start_col] == SPLIT_SYMBOL:
    active_splitter.add((i, start_col))
    break


seen = set()
def search_split(i: int, j: int) -> tuple[int, int]:
  if (i, j) in seen:
    return -1, -1
  
  seen.add((i, j))
  for ni in range(i+1, ROWS):
    if lines[ni][j] == SPLIT_SYMBOL:
      return ni, j
  
  return -1, -1


def check_both_sides(i: int, j: int) -> list[tuple[int, int]]:
  # left side
  if 0 <= j - 1: 
    li, lj = search_split(i, j-1)
  
  # right side
  if j + 1 < COLS: 
    ri, rj = search_split(i, j+1)
  
  return [(li, lj), (ri, rj)]


for i, j in splitters:
  if (i, j) not in active_splitter:
    continue
  
  left_beam, right_beam = check_both_sides(i, j)
  
  if left_beam != (-1, -1):
    active_splitter.add(left_beam)
  
  if right_beam != (-1, -1):
    active_splitter.add(right_beam)
  
    
print(f"Part One [First Approach]: {len(active_splitter)}")


###################################
## Second Approach: Using BTrees ##
###################################

class TNode:
  def __init__(self, left=None, right=None, coords=None):
    self.left = left
    self.right = right
    self.coords = coords
    

seen: dict[tuple[int, int], TNode] = {}
nodes: dict[tuple[int, int], TNode] = {}
def search_split(i: int, j: int) -> TNode | None:
  if (i, j) in seen:
    return seen[(i, j)]
  
  for ni in range(i+1, ROWS):
    if lines[ni][j] == SPLIT_SYMBOL:
      
      if (ni, j) in nodes:
        new_node = nodes[(ni, j)]
      
      else:
        new_node = TNode(coords=(ni, j))
        nodes[(ni, j)] = new_node
        
      seen[(i, j)] = new_node
      return new_node
  
  seen[(i, j)] = None
  return None


def check_both_sides(i: int, j: int) -> list[TNode | None, TNode | None]:
  
  # left side
  left_node = search_split(i, j-1)
  
  # right side
  right_node = search_split(i, j+1)
  
  return [left_node, right_node]

    
# find the first split or root node
for i in range(1, ROWS):
  if lines[i][start_col] == SPLIT_SYMBOL:
    root = TNode(coords=(i, start_col))
    break 

# build tree
nodes[root.coords] = root

visited = set()
nodes_to_explore: deque[TNode] = deque([root])
while nodes_to_explore:
  curr_node = nodes_to_explore.popleft()
  
  left_beam, right_beam = check_both_sides(*curr_node.coords)
  
  if left_beam is not None:
    curr_node.left = left_beam
    if left_beam.coords not in visited:
      nodes_to_explore.append(left_beam)
      visited.add(left_beam.coords)
  
  if right_beam is not None:
    curr_node.right = right_beam
    if right_beam.coords not in visited:
      nodes_to_explore.append(right_beam)
      visited.add(right_beam.coords)


def count_nodes(node: TNode, seen=set()) -> int:
  if node is None:
    return 0
  
  if node.coords in seen:
    return 0
  
  seen.add(node.coords)
  return 1 + count_nodes(node.left) + count_nodes(node.right)

# the answer is len(nodes)... but a recursive function is cooler
print(f"Part One [BTree Approach]: {count_nodes(root)}")


# =========== Part Two =========== #

def count_none_childs(node: TNode, memo={}) -> int:  
  if node is None:
    return 1
  
  if node.coords in memo:
    return memo[node.coords]
  
  memo[node.coords] = count_none_childs(node.left) + count_none_childs(node.right)
  return memo[node.coords]
  
print(f"Part Two [BTree Approach]: {count_none_childs(root)}")
