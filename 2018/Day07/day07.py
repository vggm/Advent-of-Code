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
            start.remove(dst) # dst node never can be a start node

# print(f"{start=}\n")

stack = []
for node in start:
    heappush(stack, (ord(node), node)) # (alphabet_order, curr_node)

path = ""
while stack:
    _, node = heappop(stack)
    
    path += node
    
    for nxt in graph[node]:
        pre_req[nxt] -= 1
        if pre_req[nxt] == 0: # does not have pre req
            heappush(stack, (ord(nxt), nxt))
    
print(f"Part One: {path}")


# =========== Part Two =========== #

STEP_DURATION, N_WORKERS = ((0, 2), (60, 5))[1] # 0 for test, 1 for input

# load pre req again
pre_req = defaultdict(int)
for line in lines:
    _, dst = re.search(r'Step ([A-Z]).*step ([A-Z])', line).groups()
    pre_req[dst] += 1

stack = []
for node in start:
    heappush(stack, (ord(node), node)) # (alphabet_order, curr_node)

workers = [[] for _ in range(N_WORKERS)]
amount = lambda x: ord(x) - ord("A") + 1

def empty_worker(workers: list[list[str, int]]) -> int:
    for i, worker in enumerate(workers):
        if len(worker) == 0:
            return i
    
    return -1

def min_steps(workers: list[list[str, int]]) -> int:
    min_step_to_finalize = 999999
    changed = False
    for worker in workers:
        if len(worker) == 0:
            continue
        
        _, steps = worker
        min_step_to_finalize = min(min_step_to_finalize, steps)
        changed = True
    
    return min_step_to_finalize if changed else -1

cnt = 0
while stack or any(workers):
    
    while stack and (pos := empty_worker(workers)) != -1:
        _, node = heappop(stack)
        workers[pos] = [node, amount(node) + STEP_DURATION]
    
    steps_to_substract = min_steps(workers)
    
    for i, worker in enumerate(workers):
        if len(worker) == 0:
            continue
        
        node, steps = worker
        steps -= steps_to_substract
        
        if steps > 0: 
            worker[1] = steps # update steps
        
        else: # steps == 0
            workers[i] = [] # free i-worker
            
            for nxt in graph[node]:
                pre_req[nxt] -= 1
                if pre_req[nxt] == 0: # does not have pre req
                    heappush(stack, (ord(nxt), nxt))
        
    cnt += steps_to_substract # add steps
            
    
print(f"Part Two: {cnt}")
