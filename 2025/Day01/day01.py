
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
  cnt += (dial_pointing == 0)
  
print(f"Part One: {cnt}")


# ============ Part Two ============ #

cnt = 0
dial_pointing = 50
for rotation in rotations:
  direction, steps_number = rotation[0], int(rotation[1:])
  total_rotations, steps_number = steps_number // max_dial, steps_number % max_dial
  print(f"{dial_pointing=}")
  print(f"{total_rotations=}")
  steps_number *= 1 if direction == "R" else -1
  print(f"{steps_number=}")
  dial_pointing += steps_number
  print(f"{dial_pointing=}")
  
  if dial_pointing < 0:
    print("+1")
    dial_pointing %= max_dial
    cnt += 1
    
  total_rotations += (dial_pointing > max_dial)
  dial_pointing %= max_dial
  print(f"{dial_pointing=}")
  
  print((dial_pointing > max_dial), (dial_pointing == 0))
  cnt += total_rotations + (dial_pointing == 0)
  print("----")
  
print(f"Part Two: {cnt}")
  