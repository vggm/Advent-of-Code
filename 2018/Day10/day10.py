import re
from collections import defaultdict
import numpy as np
import cv2 as cv


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


graph = defaultdict(int)
for i, j in points:
    graph[(i, j)] += 1

more_than_one = False

def make_move():
    more_than_one = False
    for idx, (di, dj) in enumerate(velocities):
        i, j = points[idx]
        graph[(i, j)] -= 1 # remove old position
        
        if graph[(i, j)] == 0:
            del graph[(i, j)]
        
        ni, nj = (i+di) % real_top, (j+dj) % real_right
        graph[(ni, nj)] += 1 # check the new position
        
        if not more_than_one and graph[(ni, nj)] > 1:
            more_than_one = True
        
        points[idx] = [ni, nj] # update point

for i in range(3):
    make_move()
    

    
# vt, vb, vl, vr = 100_000, 0, 100_000, 0
# for i, j in points:
#     vt = min(vt, i)
#     vb = max(vb, i)
#     vl = min(vl, j)
#     vr = max(vr, j)


# height, width = vb-vt, vr-vl

# print(f"{vt=}, {vb=}, {vl=}, {vr=}")
# print(f"Image shape: ({height:_}x{width:_})")
# print(f"Image shape: ({real_top:_}x{real_right:_})")
# mx = np.zeros((height, width), dtype=np.uint)
# mx = np.zeros((real_top, real_right), dtype=np.uint)

# for i, j in points:
#     mx[i, j] = 255

# mh, mw = real_top // 2, real_right // 2
# top_left = mx[:mh, :mw]
# top_right = mx[:mh, mw:]
# bottom_left = mx[mh:, :mw]
# bottom_right = mx[mh:, mw:]

# from matplotlib import pyplot as plt
# from collections import Counter

# cnt = {0: 0, 255: 0}
# for row in top_left:
#     for val in row:
#         cnt[val] += 1
        
# print(cnt)

# # cv.imwrite("top_left.tiff", top_left)
# # cv.imwrite("top_right.tiff", top_right)
# # cv.imwrite("bottom_left.tiff", bottom_left)
# # cv.imwrite("bottom_right.tiff", bottom_right)
