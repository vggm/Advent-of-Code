import re
from collections import defaultdict


with open("./input.txt", "r") as fr:
    lines = fr.readlines()


points = []
velocities = []
for line in lines:
    position, velocity = re.findall(r"<\s*([-]?[0-9]+),\s*([-]?[0-9]+)>", line)
    position, velocity = list(map(int, position[::-1])), list(map(int, velocity[::-1]))
    
    points.append(position)
    velocities.append(velocity)


graph = defaultdict(int)
for i, j in points:
    graph[(i, j)] += 1


def make_move():
    for idx, (di, dj) in enumerate(velocities):
        i, j = points[idx]
        graph[(i, j)] -= 1 # remove old position
        
        if graph[(i, j)] == 0:
            del graph[(i, j)]
        
        ni, nj = (i+di), (j+dj)
        
        # update point
        graph[(ni, nj)] += 1 
        points[idx] = [ni, nj]


def show_matrix(m: list[list[int]]):
    for row in m:
        for val in row:
            print(f"{' ' if val == 0 else '#'}", end=" ")
        print()
    print()
    
            
def print_map(points: list[tuple[int, int]]):
    i, j = points[0] # first point
    top, bottom, left, right = i, i, j, j
    for i, j in points:
        top = min(top, i)
        bottom = max(bottom, i)
        left = min(left, j)
        right = max(right, j)
        
    print(f"{top=}, {bottom=}, {left=}, {right=}")
    
    height, width = bottom - top + 1, right - left + 1
    print(f"{height=}, {width=}\n")
    
    m = [[0 for _ in range(width)] for _ in range(height)]
    for i, j in points:
        m[i-top][j-left] = 1

    show_matrix(m)
     

def calculate_rectangle_area() -> int:
    i, j = points[0] # first point
    top, bottom, left, right = i, i, j, j
    for i, j in points:
        top = min(top, i)
        left = min(left, j)
        right = max(right, j)
        bottom = max(bottom, i)
        
    height, width = bottom - top + 1, right - left + 1
    return height * width


from tqdm import tqdm

minimum_points_found = {}

idx_min = -1
points_with_min_area = []
min_area = calculate_rectangle_area()
for i in tqdm(range(1, 12_000), desc="Finding minimum area"):
    
    make_move()
    area = calculate_rectangle_area()
    
    if area < min_area:
        min_area = area
        points_with_min_area = points.copy()
        idx_min = i
        
        minimum_points_found[i] = points.copy()

print(f"Index with minimum area: {idx_min}\n") # 10124

# for i in range(10124):
#     make_move()
    
print_map(minimum_points_found[idx_min])
