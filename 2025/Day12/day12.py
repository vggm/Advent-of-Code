
with open("./test.txt") as fr:
  sections = fr.read().strip().split("\n\n\n")

first_section = sections[0].split("\n\n")
second_section = sections[1].split("\n")

present_shapes = [shape.split("\n")[1:] for shape in first_section]
regions = [tuple(map(int, region.split("x"))) for region in list(map(lambda x: x.split(": ")[0], second_section))]
quantities = [tuple(map(int, quantity.split(" "))) for quantity in list(map(lambda x: x.split(": ")[1], second_section))]
  
# =========== Part One =========== # 
  

# =========== Part Two =========== #

