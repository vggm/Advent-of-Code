
from functools import cache

def get_springs(filename: str) -> list[str]:
  return open(filename).read().strip().split('\n')


def calculate_spring(spring: str) -> list[int]:
  return [len(g) for g in spring.split('.') if g]


def calculate_arrangements(spring: str, groups: list[int]) -> int:
  
  @cache
  def bt(e: int, g: int, parcial: str, total: int, pt: int, last: str) -> None:
    if e == len(spring):
      if groups == calculate_spring(parcial):
        return total + 1
    else:
      
      if parcial[e] != '?':
        if parcial[e] == '#':
          if g < len(groups) and pt < groups[g]:
            total += bt(e+1, g, parcial, total, pt+1, '#')
        else:
          total += bt(e+1, g + 1 if last != '.' else g, parcial, total, 0, '.')
        return total
      
      if g < len(groups) and pt < groups[g]:
        total += bt(e+1, g, parcial[:e] + '#' + parcial[e+1:], total, pt+1, '#')
      
      total += bt(e+1, g + 1 if last != '.' else g, parcial[:e] + '.' + parcial[e+1:], total, 0, '.')
      
    return total
        
  return bt(0, 0, spring, 0, 0, '.')
  

if __name__ == '__main__':
  springs = get_springs('Day12/test')
  ans = 0
  for s in springs:
    sp, gr = s.split()
    d = calculate_arrangements(sp, list(map(int, gr.split(','))))
    ans += d
    # print(d)
  print(f'Part one: {ans}')
  
  for s in springs:
    sp, gr = s.split()
    sp = (sp + '?') * 5
    gr = (gr + ',') * 5
    sp, gr = sp[:-1], gr[:-1]
    # print(sp, gr)
    d = calculate_arrangements(sp, list(map(int, gr.split(','))))
    ans += d
  print(f'Part two: {ans}')
  