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


for i in range(3):
    make_move()


def show_matrix(m: list[list[int]]):
    for row in m:
        for val in row:
            print(f"{' ' if val == 0 else '#'}", end=" ")
        print()
    print()


def create_letter(figure: set):
    i, j = figure.pop() # first point
    top, bottom, left, right = i, i, j, j
    for i, j in figure:
        top = min(top, i)
        bottom = max(bottom, i)
        left = min(left, j)
        right = max(right, j)
    
    figure_normalized = set()
    for i, j in figure:
        figure_normalized.add((i-top, j-right))
    
    height, width = bottom - top + 1, right - left + 1 
    print(f"{height}x{width}")
    
    # m = [[0 for _ in range(width)] for _ in range(height)]
    # for i, j in figure:
    #     m[i - top][j - left] += 1
    
    # show_matrix(m)
    

seen = set()
def explore(i, j, figure: set):
    seen.add((i, j))
    figure.add((i, j))
    
    for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if (ni, nj) in graph and (ni, nj) not in seen:
            explore(ni, nj, figure)
     
    
cnt = 0
for coord, _ in graph.items():
    if coord not in seen:
        figure = set()
        explore(*coord, figure)
        create_letter(figure)
        cnt += 1

print(f"Letters found: {cnt}")
