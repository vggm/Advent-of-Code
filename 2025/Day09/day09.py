
with open("./input.txt") as fr:
  red_tiles = fr.read().strip().split("\n")
  
red_tiles = list(map(lambda x: list(map(int, x.split(","))), red_tiles))
      
  
# =========== Part One =========== #
  
def calc_area(x1, y1, x2, y2):
  return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    

print(f"Part One: {
  max(calc_area(*p1, *p2) 
    for i, p1 in enumerate(red_tiles) 
      for p2 in red_tiles[i+1:])}")


# =========== Part Two =========== #

def calc_area_points(x1, y1, x2, y2):
  top = min(y1, y2)
  left = min(x1, x2)
  right = max(x1, x2)
  bottom = max(y1, y2)
  
  tl, br = (left, top), (right, bottom)
  area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
  
  return area, tl, br



