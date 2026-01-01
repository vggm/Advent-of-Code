
from collections import deque


with open("./input.txt") as fr:
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
  
# ans = 0
# for lights, buttons, joltages in machines:
  
#   init_lights = [False] * len(lights)
  
#   found = False
#   states_seen = {tuple(init_lights)}
#   states = deque([(init_lights, 1)])
#   while states and not found: 
#     curr_state, steps = states.popleft()
    
#     for combination in buttons:
      
#       nxt_state = curr_state.copy()
#       for press in combination:
#         nxt_state[press] = not nxt_state[press]
      
#       if nxt_state == lights:
#         ans += steps
#         found = True
#         break
      
#       if tuple(nxt_state) not in states_seen:
#         states_seen.add(tuple(nxt_state))
#         states.append((nxt_state, steps + 1))
        

# print(f"Part One: {ans}")


# =========== Part Two =========== #

from concurrent.futures import ProcessPoolExecutor, Future, as_completed

def num_steps(buttons: list[list[int]], joltages: list[int], i: int) -> int:
  buttons.sort(key=len, reverse=True)

  curr_jolts = [0] * len(joltages)
  
  states_seen = set()
  
  combs = {idx: 0 for idx, _ in enumerate(buttons)}
  
  total_steps = 0
  def dfs(i: int, steps: int) -> bool:
    nonlocal total_steps, combs
    
    if tuple(curr_jolts) in states_seen:
      return False
    
    states_seen.add(tuple(curr_jolts))
    
    for idx, combination in enumerate(buttons[i:], start=i):
      for press in combination:
        curr_jolts[press] += 1
      combs[idx] += 1
      
      if all(i == j for i, j in zip(curr_jolts, joltages)):
        total_steps = steps
        return True
      
      if all(i <= j for i, j in zip(curr_jolts, joltages))\
         and dfs(idx, steps+1):
        return True
        
      for press in combination:
        curr_jolts[press] -= 1
      combs[idx] -= 1
    
    return False

  dfs(i=0, steps=1)
  return (i, total_steps)


if __name__ == "__main__":

  ans = [0] * len(machines)
  with ProcessPoolExecutor() as executor:
    
    future_to_index: dict[Future, int] = {}

    for i, (lights, buttons, joltages) in enumerate(machines):
      future = executor.submit(num_steps, buttons, joltages, i)
      future_to_index[future] = i
    
    for future in as_completed(future_to_index):
      
      try:
        i, steps = future.result()
        ans[i] = steps
      
        print(f"Finish machine {i}/{len(machines)-1}!!")
      
      except:
        pass
      

  print(f"Part Two: {sum(ans)}")
