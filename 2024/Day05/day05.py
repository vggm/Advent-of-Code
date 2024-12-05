

from collections import defaultdict, deque


def read_file(filename: str) -> list[str]:
  with open(filename, "r") as rfile:
    return rfile.readlines()


def correct(nums: list[int], rules: dict[int, set[int]]) -> list[int]:
  nums_set = set(nums)
  
  graph = defaultdict(list)
  inDegree = defaultdict(int)
  for node, adjs in rules.items():
    if node not in nums_set:
      continue
    
    for adj in adjs:
      if adj  in nums_set:
        graph[node] += [adj]
        inDegree[adj] += 1
  
  stack = deque([((nums_set - inDegree.keys()).pop(), [], 1)])
  while stack:
    node, path, n = stack.popleft()
    if n == len(nums):
      return path + [node]
    
    for nxnode in graph[node]:
      inDegree[nxnode] -= 1
      if inDegree[nxnode] == 0:
        stack.append((nxnode, path + [node] , n+1))
  
  return []


def is_correct(nums: list[int], rules: dict[int, set[int]]) -> bool:
  seen = set()
  for x in nums:
    if any(r in seen for r in rules[x]):
      return False
    seen.add(x)
  
  return True


def solve(input: list[str]) -> tuple[int, int]:
  sep = input.index('\n')
  
  rules = defaultdict(set)
  for r1, r2 in map(lambda s: list(map(int, s.strip().split('|'))), input[:sep]):
    rules[r1].add(r2)
  
  part1, part2 = 0, 0
  for nums in map(lambda s: list(map(int, s.strip().split(','))), input[sep+1:]):
    if is_correct(nums, rules):
      part1 += nums[len(nums) // 2]
    
    else:
      part2 += correct(nums, rules)[len(nums) // 2]
  
  return part1, part2


if __name__ == '__main__':
  test = read_file("./test.in")
  
  sol1, sol2 = solve(test)
  assert sol1 == 143, f"Expected 143, but got {sol1}."
  assert sol2 == 123, f"Expected 123, but got {sol2}."
  
  in1 = read_file("./in1.in")
  sol1, sol2 = solve(in1)
  print(f"Part One: {sol1}")
  print(f"Part Two: {sol2}")
  