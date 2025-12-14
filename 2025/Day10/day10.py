
from collections import deque

from tqdm import tqdm


with open("./test.txt") as fr:
  machines = fr.read().strip().split("\n")


def separate_sections(machine: str):
  machine = machine[1:-1]
  first, second = machine.split("] (")
  second, third = second.split(") {")
  return first, second, third

def process_first(first: str):
  return [c == "#" for c in first]

def process_second(second: str):
  second = second.split(") (")
  return [list(map(int, buttons.split(","))) for buttons in second]

def process_third(third: str):
  return list(map(int, third.split(",")))


machines = list(map(lambda x: (process_first(x[0]), process_second(x[1]), process_third(x[2])), map(separate_sections, machines)))

  
# =========== Part One =========== # 
  
ans = 0
for lights, buttons, joltages in machines:
  
  init_lights = [False] * len(lights)
  
  found = False
  states_seen = {tuple(init_lights)}
  states = deque([(init_lights, 1)])
  while states and not found: 
    curr_state, steps = states.popleft()
    
    for combination in buttons:
      
      nxt_state = curr_state.copy()
      for press in combination:
        nxt_state[press] = not nxt_state[press]
      
      if nxt_state == lights:
        ans += steps
        found = True
        break
      
      if tuple(nxt_state) not in states_seen:
        states_seen.add(tuple(nxt_state))
        states.append((nxt_state, steps + 1))
        

print(f"Part One: {ans}")


# =========== Part Two =========== #

ans = 0
for lights, buttons, joltages in machines:
  
  init_jolts = [0] * len(joltages)
  
  found = False
  states = deque([(init_jolts, 1)])
  states_seen = {tuple(init_jolts)}
  while states and not found: 
    curr_state, steps = states.popleft()
    
    for combination in buttons:
      
      nxt_state = curr_state.copy()
      for press in combination:
        nxt_state[press] += 1
        
      if tuple(nxt_state) in states_seen:
        continue
        
      states_seen.add(tuple(nxt_state))
      
      if all(joltages[i] % jolt == 0 for i, jolt in enumerate(nxt_state)):
        ans += steps
        found = True
        break
      
      elif all(jolt <= joltages[i] for i, jolt in enumerate(nxt_state)):
        states.append((nxt_state, steps + 1))
        

print(f"Part Two: {ans}")
