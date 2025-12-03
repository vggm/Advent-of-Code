
with open("./input.txt") as fr:
  banks_of_batteries = fr.read().strip().split("\n")

banks_of_batteries = list(map(lambda x: list(map(int, x)), map(list, banks_of_batteries)))


# =========== Part One =========== #

sum_of_joltages = 0
for bank in banks_of_batteries:
  
  l, r = 0, -1
  for idx, val in enumerate(bank[1:], start=1):
    if idx < len(bank) - 1 and val > bank[l]:
      l = idx
      r = -1
    
    elif r == -1 or val > bank[r]:
      r = idx
  
  sum_of_joltages += bank[l] * 10 + bank[r]

print(f"Part One: {sum_of_joltages}")


# =========== Part Two =========== #

import numpy as np

num_len = 12

sum_of_joltages = 0
for bank in banks_of_batteries:
  num = 0
  
  curr = 0
  last = -1
  while curr < num_len:
    best_idx = np.argmax(bank[last+1:-11+curr if -11+curr < 0 else len(bank)]) + last + 1
    num += bank[best_idx] * 10 ** (num_len - 1 - curr)
    last = best_idx
    
    curr += 1
  
  sum_of_joltages += num
      
print(f"Part Two: {sum_of_joltages}")
