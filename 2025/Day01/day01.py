

with open("./test.txt") as fr:
  rotations = fr.read().strip().split("\n")

max_dial = 100

# ============ Part One ============ #

cnt = 0
dial_pointing = 50
for rotation in rotations:
  direction, steps_number = rotation[0], int(rotation[1:])
  steps_number *= 1 if direction == "R" else -1
  
  dial_pointing = (dial_pointing + steps_number) % max_dial
  if dial_pointing == 0:
    cnt += 1
  
print(f"Part One: {cnt}")


# ============ Part One ============ #

cnt = 0
dial_pointing = 50
for rotation in rotations:
  direction, steps_number = rotation[0], int(rotation[1:])
  steps_number *= 1 if direction == "R" else -1
  
  dial_pointing += steps_number
  
  total_rotations, dial_pointing = abs(dial_pointing // max_dial), dial_pointing % max_dial
  
  cnt += total_rotations + dial_pointing == 0
  
print(f"Part Two: {cnt}")
  