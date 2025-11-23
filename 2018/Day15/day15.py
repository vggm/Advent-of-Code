import sys
from heapq import heappush, heappop, heapify


HEALTH, DAMAGE = 200, 3


if len(sys.argv) < 2:
  print("Argument Error!")
  print("Usage: python3 day15.py (input_filename)")
  sys.exit(1)
  
file = sys.argv[1]

with open(file) as fr:
  m = list(map(lambda s: list(s.strip()), fr.read().strip().split("\n")))

def show_matrix(m: list[list[str]], idx=0):
  print("=" * 12, idx, "=" * 12)
  for row in m:
    print(*row)
  print("=" * 27)

show_matrix(m, "init state")


# ============= Part One ============= #

HEALTH_POS, ENT_POS = 0, 1

entities: dict[tuple[int, int], list[int, str]] = {}
for i, row in enumerate(m):
  for j, val in enumerate(row):
    if val in ["E", "G"]:
      entities[(i, j)] = [HEALTH, val]

def can_attack(i: int, j: int, ent: str) -> tuple[int, int] | None:
  
  possible = []
  for ai, aj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
    if m[ai][aj] not in ["#", "."] and m[ai][aj] != ent: 
      possible.append((ai, aj))
  
  if not possible:
    return None
  
  min_coord = possible[0]
  min_hp = entities[*possible[0]][0]
  for ni, nj in possible:
    if entities[(ni, nj)][HEALTH_POS] < min_hp:
      min_hp = entities[(ni, nj)][HEALTH_POS]
      min_coord = (ni, nj)
  
  return min_coord
  
def attack(i: int, j: int, damage=3) -> bool:
  target_hp, target_ent = entities[(i, j)]
  target_hp -= damage
  
  entities[(i, j)] = [target_hp, target_ent]
  return target_hp <= 0
  
def exist_enemies(ent: str) -> bool:
  return any(ent != other_ent for _, other_ent in entities.values())
  
def nearest_point(i: int, j: int, ent: str) -> tuple[int, int]:
  seen: set[tuple[int, int]] = set()
  stack = [(0, i, j, [])]
  while stack:
    d, i, j, p = heappop(stack)
    if (i, j) in seen:
      continue
    seen.add((i, j))
    
    for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
      if m[ni][nj] not in ["#", ent]:
        if m[ni][nj] == ".":
          heappush(stack, (d+1, ni, nj, p + [(ni, nj)]))
                  
        else: # not ent
          return ni, nj, p
  
  return -1, -1, []

def make_move(oi: int, oj: int, ni: int, nj: int):
  ent = m[oi][oj]
  m[oi][oj] = '.'
  m[ni][nj] = ent
  
  tmp = entities[(oi, oj)]
  entities[(ni, nj)] = tmp
  del entities[(oi, oj)]

  
end = False
game_rounds = -1
while not end:
  entities_coords = sorted(entities.keys())
  
  game_rounds += 1
  someone_has_died = False

  for idx, (i, j) in enumerate(entities_coords):
    # print(i, j)
    hp, ent = entities[(i, j)]
    # print(f"   {hp=}, {ent=}")
    if hp <= 0:
      # print("dead")
      continue
     
    if not exist_enemies(ent):
      if idx == 0:
        game_rounds -= 1
      end = True
      break
    
    if target := can_attack(i, j, ent):
      ti, tj = target
      # print(f"attack {ti}, {tj}")
      has_died = attack(ti, tj)
      if not someone_has_died and has_died:
        # print("killed")
        m[ti][tj] = "." # remove from the map
        someone_has_died = True
      continue
    
    *nearest_target, path = nearest_point(i, j, ent)
    if nearest_target == [-1, -1]:
      # print("cannot move")
      continue
    
    ni, nj = path[0]
    # print(f"move to {ni}, {nj}")
    make_move(i, j, ni, nj)
    
    i, j = ni, nj
    if target := can_attack(i, j, ent):
      ti, tj = target
      # print(f"attack {ti}, {tj}")
      has_died = attack(ti, tj)
      if not someone_has_died and has_died:
        # print("killed")
        m[ti][tj] = "." # remove from the map
        someone_has_died = True
  
  # print(entities)
  # show_matrix(m, game_rounds)
  
  if someone_has_died:   
    remove = []
    for key, (hp, _) in entities.items():
      if hp <= 0:
        remove.append(key)
    
    for key in remove:
      del entities[key]

print(entities)
print(f"rounds: {game_rounds}, hp sum: {sum(hp for hp, _ in entities.values())}")
print(f"Part One: {game_rounds * sum(hp for hp, _ in entities.values())}")


# ============= Part Two ============= #

from copy import deepcopy

with open(file) as fr:
  init_map = list(map(lambda s: list(s.strip()), fr.read().strip().split("\n")))

num_of_elfs = sum(1 for row in init_map for val in row if val == 'E')
  
L, R = 4, 50
while L <= R:
  curr_damage = (L + R) // 2
  print(curr_damage)
  
  m = deepcopy(init_map)

  entities: dict[tuple[int, int], list[int, str]] = {}
  for i, row in enumerate(m):
    for j, val in enumerate(row):
      if val in ["E", "G"]:
        entities[(i, j)] = [HEALTH, val]

  end = False
  game_rounds = -1
  while not end:
    entities_coords = sorted(entities.keys())
    
    game_rounds += 1
    someone_has_died = False

    for idx, (i, j) in enumerate(entities_coords):
      
      hp, ent = entities[(i, j)]
      if hp <= 0:
        continue
      
      attack_damage = curr_damage if ent == "E" else 3
      
      if not exist_enemies(ent):
        if idx == 0:
          game_rounds -= 1
        end = True
        break
      
      if target := can_attack(i, j, ent):
        ti, tj = target        
        if has_died := attack(ti, tj, damage=attack_damage):
          m[ti][tj] = "." # remove from the map
        if not someone_has_died and has_died:
          someone_has_died = True
        continue
      
      *nearest_target, path = nearest_point(i, j, ent)
      if nearest_target == [-1, -1]:
        continue
      
      ni, nj = path[0]
      make_move(i, j, ni, nj)
      
      i, j = ni, nj
      if target := can_attack(i, j, ent):
        ti, tj = target
        if has_died := attack(ti, tj, damage=attack_damage):
          m[ti][tj] = "." # remove from the map
        if not someone_has_died and has_died:
          someone_has_died = True
    
    if someone_has_died:   
      remove = []
      for key, (hp, _) in entities.items():
        if hp <= 0:
          remove.append(key)
      
      for key in remove:
        del entities[key]
    
  if num_of_elfs == sum(1 for _, ent in entities.values() if ent == "E"):
    R = curr_damage - 1
  
  else:
    L = curr_damage + 1
  

print(f"Minor DAMAGE to WIN: {L}")

curr_damage = L
m = deepcopy(init_map)

entities: dict[tuple[int, int], list[int, str]] = {}
for i, row in enumerate(m):
  for j, val in enumerate(row):
    if val in ["E", "G"]:
      entities[(i, j)] = [HEALTH, val]

end = False
game_rounds = -1
while not end:
  entities_coords = sorted(entities.keys())
  
  game_rounds += 1
  someone_has_died = False

  for idx, (i, j) in enumerate(entities_coords):
    
    hp, ent = entities[(i, j)]
    if hp <= 0:
      continue
    
    attack_damage = curr_damage if ent == "E" else 3
    
    if not exist_enemies(ent):
      if idx == 0:
        game_rounds -= 1
      end = True
      break
    
    if target := can_attack(i, j, ent):
      ti, tj = target        
      if has_died := attack(ti, tj, damage=attack_damage):
        m[ti][tj] = "." # remove from the map
      if not someone_has_died and has_died:
        someone_has_died = True
      continue
    
    *nearest_target, path = nearest_point(i, j, ent)
    if nearest_target == [-1, -1]:
      continue
    
    ni, nj = path[0]
    make_move(i, j, ni, nj)
    
    i, j = ni, nj
    if target := can_attack(i, j, ent):
      ti, tj = target
      if has_died := attack(ti, tj, damage=attack_damage):
        m[ti][tj] = "." # remove from the map
      if not someone_has_died and has_died:
        someone_has_died = True
  
  if someone_has_died:   
    remove = []
    for key, (hp, _) in entities.items():
      if hp <= 0:
        remove.append(key)
    
    for key in remove:
      del entities[key]

print(entities)
print(f"rounds: {game_rounds}, hp sum: {sum(hp for hp, _ in entities.values())}")
print(f"Part Two: {game_rounds * sum(hp for hp, _ in entities.values())}")
