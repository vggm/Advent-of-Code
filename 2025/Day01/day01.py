
with open("./input.txt") as fr:
  rotations = fr.read().strip().split("\n")

max_dial = 100


# ============ Part One ============ #

cnt = 0
dial_pointing = 50
for rotation in rotations:
  direction, steps_number = rotation[0], int(rotation[1:])
  steps_number *= 1 if direction == "R" else -1
  
  dial_pointing = (dial_pointing + steps_number) % max_dial
  cnt += (dial_pointing == 0)
  
print(f"Part One: {cnt}")


# ============ Part Two ============ #

cnt = 0
dial_pointing = 50
for rotation in rotations:
  direction, steps_number = rotation[0], int(rotation[1:])
  
  total_rotations = steps_number // max_dial # doesnt need to do the rotations
  steps_number = steps_number % max_dial # just need the steps lesser than max dial

  steps_number *= 1 if direction == "R" else -1

  dial_pointing += steps_number
  
  if dial_pointing < 0:
    cnt += (dial_pointing - steps_number != 0) # only if prev dial pointing DOESNT start at 0
    dial_pointing %= max_dial # normalize dial pointing
  
  else:  
    total_rotations += (dial_pointing > max_dial) # if the sum is greater than max
    dial_pointing %= max_dial # normalize
  
  is_poiting_at_0 = (dial_pointing == 0) # check if the dial is pointing at 0
  cnt += total_rotations + is_poiting_at_0
  
print(f"Part Two: {cnt}")
  