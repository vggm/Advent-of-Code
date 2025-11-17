

with open("test.txt", "r") as fr:
  lines = fr.read().strip().split("\n")


initial_state = lines[0].split(": ")[1]
print(initial_state)

patterns = list(map(lambda x: x.split(" => "), lines[2:]))
pattern2out = {pattern: output for pattern, output in patterns}

N_GENERATIONS = 20
SLIDE_SIZE = 5

total_sum = 0
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
  total_sum += curr_state.count("#")
  print(curr_state)


print(f"Part One: {total_sum}")
