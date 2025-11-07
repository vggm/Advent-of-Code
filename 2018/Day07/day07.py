import re
from collections import defaultdict 
from heapq import heappush, heappop

with open("./test.txt", "r") as fr:
    lines = fr.readlines()

nodes = set()
graph = defaultdict(set)
for line in lines:
    org, dst = re.search(r'Step ([A-Z]).*step ([A-Z])', line).groups()
    graph[org] |= {dst}
    nodes |= {org, dst}


# =========== Part One =========== #

print("Graph:")
for key, values in graph.items():
    print(f"{key}: {values}")
print()

start: set[str] = nodes.copy()
for org, dst in graph.items():
    start ^= dst

print(f"{start=}")

start: str = start.pop()
seen: set[str] = set()

# (alphabet_order, curr_node, path)
stack = [(ord(start), start, "")]
while stack:
    _, node, path = heappop(stack)
    print(node)
    
    if node in seen:
        continue
    seen.add(node)
    
    path += node
    
    if len(path) == len(nodes):
        break
    
    for nxt in graph[node]:
        heappush(stack, (ord(nxt), nxt, path))
    
print(f"Part One: {path}")
