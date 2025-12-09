
with open("./input.txt") as fr:
  red_tiles = fr.read().strip().split("\n")
  
red_tiles = list(map(lambda x: list(map(int, x.split(","))), red_tiles))
      
  
# =========== Part One =========== #
  
max_area = 0

for i, (x1, y1) in enumerate(red_tiles):
  for (x2, y2) in red_tiles[i+1:]:
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    max_area = max(max_area, area)
    

print(f"Part One: {max_area}")


# =========== Part Two =========== #

 
