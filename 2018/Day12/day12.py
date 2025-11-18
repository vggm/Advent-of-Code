

with open("input.txt", "r") as fr:
  lines = fr.read().strip().split("\n")


initial_state = lines[0].split(": ")[1]

patterns = list(map(lambda x: x.split(" => "), lines[2:]))
pattern2out = {pattern: output for pattern, output in patterns if output != "."}

N_GENERATIONS = 1000
SLIDE_SIZE = 5

curr_state = initial_state
for _ in range(N_GENERATIONS):
  
  curr_state = "." * SLIDE_SIZE + curr_state + "." * SLIDE_SIZE
  nxt_state = ["."] * len(curr_state)
  
  l, r = 0, SLIDE_SIZE
  while r < len(curr_state):
    slide = curr_state[l:r]

    if slide in pattern2out: 
      m = (l+r) // 2
      nxt_state[m] = pattern2out[slide]
    
    l += 1
    r += 1

  l, r = 0, len(curr_state) - 1
  while (nxt_state[l] == "." or nxt_state[r] == ".") and l <= r:
    if nxt_state[l] == ".":
      l += 1
    
    if nxt_state[r] == ".":
      r -= 1     
  
  curr_state = "".join(nxt_state[l:r+1])

max_len = len(curr_state)


total_len = max_len * 2
curr_state = "." * max_len + initial_state + "." * max_len

position_zero = max_len

for _ in range(N_GENERATIONS):
  nxt_state = ["."] * len(curr_state)
  
  l, r = 0, SLIDE_SIZE
  while r < len(curr_state):
    slide = curr_state[l:r]

    if slide in pattern2out: 
      m = (l+r) // 2
      nxt_state[m] = pattern2out[slide]
    
    l += 1
    r += 1
  
  curr_state = "".join(nxt_state)
  # print(curr_state)
  
  total_sum = 0
  for i, val in enumerate(curr_state):
    if val == ".":
      continue
    
    pot_position = i - position_zero
    total_sum += pot_position
  print(total_sum)


total_sum = 0
for i, val in enumerate(curr_state):
  if val == ".":
    continue
  
  pot_position = i - position_zero
  total_sum += pot_position


print(f"Part One: {total_sum}")
