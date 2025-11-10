import re

with open("./test.txt", "r") as fr:
    lines = fr.readlines()


POSITION, VELOCITY = 0, 1

points = []
for line in lines:
    position, velocity = re.findall(r"<\s*([-]?[0-9]+),\s*([-]?[0-9]+)>", line)
    position, velocity = list(map(int, position)), list(map(int, velocity))
    
    # print(position, velocity)
    
    points.append([position, velocity])

top, right = 0, 0 # limits
for (j, i), (_, _) in points:
    top = max(top, i)
    right = max(right, j)

m = [["." for _ in range(right + 1)] for _ in range(top + 1)]

for (j, i), (_, _) in points:
    m[i][j] = "#"
    
for row in m:
    for val in row:
        print(val, end=" ")
    print()

