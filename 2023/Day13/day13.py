

def get_groups(filename: str) -> list[list[str]]:
  return [g.split() for g in open(filename).read().split('\n\n')]


def check_reflection(mirror: list[str]) -> int:
  nrow = 0
  found = False
  
  for curr, row1 in enumerate(mirror[:-1]):
    row2 = mirror[curr+1]
    
    if (row1 == row2):
      enc = True
      t, b = curr, curr+1
      while t > 0 and b < len(mirror)-1 and enc:
        t -= 1
        b += 1
        
        if mirror[t] != mirror[b]:
          enc = False
          
      found = enc
    
    if found:
      nrow = curr + 1
      break
    
    
  return nrow if found else -1


def check_reflection_smudge(mirror: list[str]) -> int:
  nrow = 0
  found = False
  
  for curr, row1 in enumerate(mirror[:-1]):
    row2 = mirror[curr+1]
    
    if row1 == row2 or 1 == sum(1 if x1 != x2 else 0 for x1, x2 in zip(row1, row2)):
      first = row1 == row2
      enc = True
      t, b = curr, curr+1
      while t > 0 and b < len(mirror)-1 and enc:
        t -= 1
        b += 1
        
        if mirror[t] != mirror[b]:
          if first and 1 == sum(1 if x1 != x2 else 0 for x1, x2 in zip(mirror[t], mirror[b])):
            first = False
          else:
            enc = False
          
      found = enc and not first
    
    if found:
      nrow = curr + 1
      break
    
    
  return nrow if found else -1


def part_one(mirrors: list[list[str]]) -> int:
  cnt = 0
  for mirror in mirrors:
    value = check_reflection([''.join(v for v in row) for row in list(zip(*mirror))])
    if value != -1:
      cnt += value
    else:
      cnt += check_reflection(mirror) * 100
  return cnt


def part_two(mirrors: list[list[str]]) -> int:
  cnt = 0
  for mirror in mirrors:
    temp1 = check_reflection_smudge([''.join(v for v in row) for row in list(zip(*mirror))])
    
    if temp1 != -1:
      value = temp1
    else:
      value = check_reflection_smudge(mirror) * 100

    cnt += value
  return cnt
    

if __name__ == '__main__':
  grps = get_groups('Day13/input.txt')
  print(f'Part one: {part_one(grps)}')
  print(f'Part two: {part_two(grps)}')
    