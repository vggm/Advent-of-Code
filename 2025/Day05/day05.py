
with open("./input.txt") as fr:
  fresh_list, IDs = fr.read().strip().split("\n\n")

fresh_list = list(map(lambda x: [int(y) for y in x], map(lambda x: x.split("-"), fresh_list.split("\n"))))
IDs = list(map(int, IDs.split("\n")))


# =========== Part One =========== #

cnt = 0
for ingredient in IDs:
  for l1, l2 in fresh_list:
    if l1 <= ingredient <= l2:
      cnt += 1
      break
    
print(f"Part One: {cnt}")


# =========== Part Two =========== #

fresh_list.sort()
fresh_list_opt = []

L, R = fresh_list[0]
for l1, l2 in fresh_list[1:]:
  if R < l1: # cannot join, its a new range
    fresh_list_opt.append((L, R)) # save last range
    L, R = l1, l2 # start the new range
    
  else:
    R = max(R, l2) # join ranges if l2 > R2, else L <= l1, l2 <= R

fresh_list_opt.append((L, R))
      
print(f"Part Two: {sum(R-L+1 for L, R in fresh_list_opt)}")
