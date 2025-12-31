
with open("./input.txt") as fr:
  sections = fr.read().strip().split("\n\n\n")

first_section = sections[0].split("\n\n")
second_section = sections[1].split("\n")

present_shapes = [shape.split("\n")[1:] for shape in first_section]
present_area = [sum(row.count("#") for row in shape) for shape in present_shapes]

regions = [tuple(map(int, region.split("x"))) for region in list(map(lambda x: x.split(": ")[0], second_section))]
quantities = [tuple(map(int, quantity.split(" "))) for quantity in list(map(lambda x: x.split(": ")[1], second_section))]
  
  
# =========== Part One =========== # 
  
valid_regions = 0
for (height, width), list_of_quantity in zip(regions, quantities):
  area = height * width
  sum_area = sum(present_area[idx] * qnt for idx, qnt in enumerate(list_of_quantity))
  
  if sum_area <= area:
    valid_regions += 1

print(f"Part One: {valid_regions}")


# =========== Part Two =========== #

