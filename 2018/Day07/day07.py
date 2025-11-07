import re
from collections import defaultdict 
from heapq import heappush, heappop

with open("./input.txt", "r") as fr:
    lines = fr.readlines()

nodes = set()
graph = defaultdict(set)
pre_req = defaultdict(int)
for line in lines:
    org, dst = re.search(r'Step ([A-Z]).*step ([A-Z])', line).groups()
    
    pre_req[dst] += 1
    graph[org] |= {dst}
    nodes |= {org, dst}


# =========== Part One =========== #

# print("Graph:")
# for key, values in graph.items():
#     print(f"{key}: {values}")
# print()

# print("Pre Req:")
# for key, value in pre_req.items():
#     print(f"{key}: {value}")
# print()

start: set[str] = nodes.copy()
for org, dst_list in graph.items():
    for dst in dst_list:
        if dst in start:
            start.remove(dst) # dst node never must be a start node

# print(f"{start=}\n")

stack = []
for node in start:
    #               (alphabet_order, curr_node)
    heappush(stack, (ord(node), node))

path = ""
while stack:
    _, node = heappop(stack)
    
    path += node
    
    for nxt in graph[node]:
        pre_req[nxt] -= 1
        if pre_req[nxt] == 0: # does not have pre req
            heappush(stack, (ord(nxt), nxt))
    
print(f"Part One: {path}")
