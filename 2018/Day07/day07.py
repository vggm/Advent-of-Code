import re
from collections import defaultdict 

with open("./test.txt", "r") as fr:
    lines = fr.readlines()

nodes = set()
graph = defaultdict(set)
for line in lines:
    org, dst = re.search(r'Step ([A-Z]).*step ([A-Z])', line).groups()
    graph[org] |= {dst}
    nodes |= {org, dst}

print("Graph:")
for key, values in graph.items():
    print(f"{key}: {values}")
print()

start = nodes.copy()
for org, dst in graph.items():
    start ^= dst

print(f"{start=}")
