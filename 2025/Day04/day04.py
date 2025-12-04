
with open("./input.txt") as fr:
  m = fr.read().strip().split("\n")

m = list(map(list, m))


# =========== Part One =========== #

cnt = 0
for i, row in enumerate(m):
  for j, val in enumerate(row):
    
    if val == ".":
      continue
    
    next_coords = [
      (i-1, j-1),  # top left
      (i-1, j),    # top
      (i-1, j+1),  # top right
      (i, j-1),    # left
      (i, j+1),    # right
      (i+1, j-1),  # bottom left
      (i+1, j),    # bottom
      (i+1, j+1)   # bottom right
    ]
    
    roll_papers = sum(1 
        for ni, nj in next_coords
          if 0 <= ni < len(m) and 0 <= nj < len(m[0]) and m[ni][nj] == "@")
  
    if roll_papers < 4: # can be lifted
      cnt += 1
      
      
print(f"Part One: {cnt}")


# =========== Part Two =========== #

cnt = 0
while True:
  
  roll_papers_to_remove = []
  
  for i, row in enumerate(m):
    for j, val in enumerate(row):
      
      if m[i][j] == ".":
        continue
      
      next_coords = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
      
      roll_papers = sum(1 
          for ni, nj in next_coords
            if 0 <= ni < len(m) and 0 <= nj < len(m[0]) and m[ni][nj] == "@")
    
      if roll_papers < 4:
        roll_papers_to_remove.append((i, j)) # can be lifted
        cnt += 1
  
  if len(roll_papers_to_remove) == 0: # end loop
    break
  
  # remove roll papers that can be lifted for the next iteration
  for i, j in roll_papers_to_remove:
    m[i][j] = "."

      
print(f"Part Two: {cnt}")
