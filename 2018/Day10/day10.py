import re

with open("./input.txt", "r") as fr:
    lines = fr.readlines()


points = []
velocities = []
for line in lines:
    position, velocity = re.findall(r"<\s*([-]?[0-9]+),\s*([-]?[0-9]+)>", line)
    position, velocity = list(map(int, position[::-1])), list(map(int, velocity[::-1]))
    
    # print(position, velocity)
    
    points.append(position)
    velocities.append(velocity)

top, bottom, right, left = 0, 0, 0, 0 # limits
for i, j in points:
    top = max(top, i)
    left = min(left, j)
    right = max(right, j)
    bottom = min(bottom, i)

real_top = abs(bottom) + top + 1
real_right = abs(left) + right + 1

# re-ajust the points knowing the perspective from the observer
for position in points:
    position[0] -= bottom
    position[1] -= left

print(f"{top=}, {bottom=}, {left=}, {right=}\n{real_top=}, {real_right=}\n")
m = [[0 for _ in range(real_right)] for _ in range(real_top)]

for i, j in points:
    m[i][j] = 1

def show_matrix(idx="#"):
    print("=" * 20, str(idx), "=" * 20)
    for row in m:
        for val in row:
            print(f"{"#" if val > 0 else "."}", end=" ")
        print()
    print("=" * 43)
    
# show_matrix(0)

more_than_one = False

def make_move():
    more_than_one = False
    for idx, (di, dj) in enumerate(velocities):
        i, j = points[idx]
        m[i][j] -= 1 # remove old position
        
        ni, nj = (i+di) % real_top, (j+dj) % real_right
        m[ni][nj] += 1 # check the new position
        
        if not more_than_one and m[ni][nj] > 1:
            more_than_one = True
        
        points[idx] = [ni, nj] # update point
    
# make_move()
# show_matrix()


def is_two_island() -> bool:
    cnt = 0
    seen = set()
    
    def explore(i, j):
        nonlocal seen
        seen.add((i, j))
        
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < real_top and 0 <= nj < real_right and m[ni][nj] == 1 and (ni, nj) not in seen:
                explore(ni, nj)
    
    for i in range(real_top):
        for j in range(real_right):
            if m[i][j] == 1 and (i, j) not in seen:
                explore(i, j)
                cnt += 1
                if cnt > 2:
                    return False
    return True

from tqdm import tqdm

for i in tqdm(range(1, 10_000)):
    
    if i % 1000 == 0:
        print(i)
    
    make_move()
    
    if not more_than_one and is_two_island():
        show_matrix(i)
        