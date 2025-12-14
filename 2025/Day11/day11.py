
from collections import deque


def load_data(file: str) -> dict:
  
  with open(file) as fr:
    lines = fr.read().strip().split("\n")
    
  def process_line(line: str) -> tuple[str, list[str]]:
    node, adjs = line.split(": ")
    adjs = adjs.split(" ")
    return node, adjs
  
  graph_conf = list(map(process_line, lines))
  return {node: adjs for node, adjs in graph_conf}

graph = load_data("./input.txt")
  
  
# =========== Part One =========== # 

ans = 0
stack = deque(["you"])
while stack:
  node = stack.popleft()
  
  if node == "out":
    ans += 1
    continue
  
  for nxt in graph[node]:
    stack.append(nxt)

print(f"Part One: {ans}")
  

# =========== Part Two =========== #

graph = load_data("./input.txt")

ans = 0
stack = deque([("svr", False, False)])
while stack:
  node, fft, dac = stack.popleft()
  
  if node == "out":
    ans += (fft and dac)
    continue
  
  for nxt in graph[node]:
    nx_fft = fft if fft else node == "fft"
    nx_dac = dac if dac else node == "dac"
    stack.append((nxt, nx_fft, nx_dac))


print(f"Part Two: {ans}")
