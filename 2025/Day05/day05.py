
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

cnt = 0
      
print(f"Part Two: {cnt}")
