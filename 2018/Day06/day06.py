from collections import defaultdict, deque
from heapq import heappop, heappush

with open("./test.txt", "r") as fr:
    lines = fr.readlines()

top, right = 0, 0
coords = list(map(lambda x: list(map(int, x.split(", "))), lines))

for j, i in coords:
    top = max(i, top)
    right = max(j, right)
    
print(f"Matrix: rows={top}, cols={right}")

outside_areas_id: list[int] = []
area: defaultdict[int] = defaultdict(int)
for i in range(top + 1):
    for j in range(right + 1):
        min_distances = sorted([(abs(i - coord_i) + (j - coord_j), coord_id) 
                                    for coord_id, (coord_i, coord_j) in enumerate(coords)])
        if len(min_distances) == 1 or min_distances[0][1] == min_distances[1][1]:
            area[i] += 1
            
            if i == 0 or j == 0 or i == top or j == right:
                outside_areas_id.append(min_distances[0][1])


max_inside_area = max([A for coord_id, A in area if coord_id not in outside_areas_id])
print(f"Part One: {max_inside_area}")

# MAX_INT = 9999999
# VALUE, VIEW = 0, 1

# m: list[list[list[int, str]]] = [
#     [[MAX_INT, '.'] 
#         for _ in range(r+2)] 
#             for _ in range(t+2)]

# total_areas = 0
# stack = []
# for j, i in coords:
#     total_areas += 1
#     m[i][j] = [MAX_INT, total_areas]
#     heappush(stack, (0, i, j, f"{total_areas}"))

# def print_matrix(m: list[list[tuple[int, str]]]):
#     display = ""
#     for row in m:
#         for (_, view) in row:
#             display += f"{view} "
#         display += "\n"
    
#     print(display)

# #print_matrix(m)

# cols, rows = len(m[0]), len(m)
# while stack:
#     d, i, j, v = heappop(stack)
    
#     if d < m[i][j][VALUE]:
#         m[i][j][VALUE] = d
#         m[i][j][VIEW] = v
    
#     elif d == m[i][j][VALUE] and m[i][j][VIEW] != v:
#         m[i][j][VIEW] = "."
    
#     for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
#         if not (0 <= ni < rows and 0 <= nj < cols):
#             continue
        
#         nd = m[ni][nj][VALUE]
#         if d + 1 <= nd and m[ni][nj][VIEW] != v:
#             heappush(stack, (d + 1, ni, nj, v))
    
#     # print_matrix(m)

# #print_matrix(m)

# seen: set[tuple[int, int]] = set()
# area: dict[str, int] = defaultdict(int)
# inside: dict[str, int] = {f"{view}": True 
#                             for view in range(1, total_areas + 1)}


# def explore(i: int, j: int, view: str):
#     area[view] += 1
#     seen.add((i, j))
    
#     for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
#         if 0 <= ni < rows and 0 <= nj < cols:
#             if m[ni][nj][VIEW] == view and (ni, nj) not in seen:
#                 explore(ni, nj, view)
        
#         else:
#             inside[view] = False
    
# for i, row in enumerate(m):
#     for j, (_, view) in enumerate(row):
#         if view == ".":
#             continue
        
#         if (i, j) not in seen:
#             explore(i, j, view)     

# max_inside_area = 0
# for key, val in inside.items():
#     print(f"Area {key}: {"Inside" if val else "Outside"}")
#     if inside[key]:
#         max_inside_area = max(area[key], max_inside_area)

# print(f"\nPart One: {max_inside_area}")
            
