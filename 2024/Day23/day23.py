from collections import defaultdict
import sys
import pyperclip as cp
import rich as rh


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

def part_one(connections: list[str]) -> int:
  
  graph = defaultdict(set)
  for src, dst in map(lambda x: x.split("-"), connections):
    graph[src].add(dst)
    graph[dst].add(src)
  
  triplets = set()
  nodes = list(graph.keys())
  for i, a in enumerate(nodes[:-2]):
    for j, b in enumerate(nodes[i+1:-1], start=i+1):
      for c in nodes[j+1:]:
        if c in graph[a] and b in graph[a] and b in graph[c]:
          if a[0] == "t" or b[0] == "t" or c[0] == "t":
            triplets.add((a, b, c))
  
  return len(triplets)


def part_two(connections: list[str]) -> int:
  
  graph = defaultdict(set)
  for src, dst in map(lambda x: x.split("-"), connections):
    graph[src].add(dst)
    graph[dst].add(src)
    
  rh.print(graph)
  
  for src in graph:
    for dst in graph[src]:
      print(graph[src] & graph[dst], ": ", len(graph[src] & graph[dst]))
  
  return -1


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  file_input = read_file(sys.argv[1])
  # pr("Part One:", part_one(file_input))
  pr("Part Two:", part_two(file_input))
  