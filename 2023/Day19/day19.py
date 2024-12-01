
from collections import defaultdict


def get_workflows_parts (filename: str) -> (dict, list[dict]):
  workflows_str, parts_str = open(filename).read().strip().split('\n\n')
  workflows, parts = defaultdict(list), []
  for lane in workflows_str.split('\n'):
    key, other = lane[:-1].split('{')
    for rule in other.split(','):
      if rule.count(':') != 0:
        workflows[key].append(rule.split(':'))
      else:
        workflows[key].append(rule)
  
  for index, lane in enumerate(parts_str.split('\n')):
    lane = lane[1:-1]
    parts.append({})
    for var in lane.split(','):
      v, n = var.split('=')
      parts[index][v] = int(n)
  
  return workflows, parts


def calculate_sum(part: dict) -> int:
  return sum(v for _, v in part.items())


def part_one(workflows: dict, parts: list[dict]) -> int:
  total = 0
  
  def find_path (part: dict) -> int:
    curr = workflows['in']
    while True:
      for condition in curr:
        if type(condition) is list:
          con, nxt = condition
          if '>' in con:
            k, n = con.split('>')
            if not part[k] > int(n):
              continue
            if nxt in ['A', 'R']:
              return calculate_sum(part) if nxt == 'A' else 0
            break
            
          else:
            k, n = con.split('<')
            if not part[k] < int(n):
              continue
            if nxt in ['A', 'R']:
              return calculate_sum(part) if nxt == 'A' else 0
            break
          
        else:
          if condition in ['A', 'R']:
            return calculate_sum(part) if condition == 'A' else 0
          else:
            nxt = condition

      curr = workflows[nxt]
  
  for part in parts:
    total += find_path(part)  
  
  return total


def main():
  W, P = get_workflows_parts('./Day19/input.txt')
  print(f'Part one: {part_one(W, P)}')
  

if __name__ == '__main__':
  main()