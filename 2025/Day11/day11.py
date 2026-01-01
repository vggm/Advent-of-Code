
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

from functools import cache


@cache
def steps_to(org: str, dst: str, avoid: tuple[str]) -> int:
  
  if org in avoid:
    return 0
  
  if org == dst:
    return 1
  
  return sum(steps_to(nxt, dst, avoid) for nxt in graph[org])


svr_fft = steps_to("svr", "fft", ("dac", "out"))
svr_dac = steps_to("svr", "dac", ("fft", "out"))
fft_dac = steps_to("fft", "dac", ("svr", "out"))
dac_fft = steps_to("dac", "fft", ("svr", "out"))
fft_out = steps_to("fft", "out", ("svr", "dac"))
dac_out = steps_to("dac", "out", ("svr", "fft"))


print(f"Part Two: {svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out}")
