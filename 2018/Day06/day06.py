from collections import defaultdict, deque


LIMIT = (32, 10000)[1] # 0 for test, 1 for input
with open("./input.txt", "r") as fr:
    lines = fr.readlines()

top, right = 0, 0
coords = list(map(lambda x: list(map(int, x.split(", "))), lines))

coords_to_id = {}
for coord_id, (j, i) in enumerate(coords, start=1):
    top = max(i, top)
    right = max(j, right)
    coords_to_id[(i, j)] = coord_id


# =========== PART 1 ===========

outside_areas_id = set()
area_size = defaultdict(int)
for i in range(top + 1):
    for j in range(right + 1):
        min_dists = sorted([
            (
                abs(i - coord_i) + abs(j - coord_j),  # manhattan distance
                coord_id,                             # coord id
            ) 
            for (coord_i, coord_j), coord_id in coords_to_id.items()])
        
        # check if there is not same distance from two coords
        if min_dists[0][0] != min_dists[1][0]:
            # get the id from the min distance
            coord_id = min_dists[0][1]
            area_size[coord_id] += 1 
        
            # check infinite area
            if i == 0 or i == top or j == 0 or j == right:
                outside_areas_id.add(coord_id)


print(f"Part One: {max(
    area 
        for coord_id, area in area_size.items() 
            if coord_id not in outside_areas_id)}")


# =========== PART 2 ===========

coords_less_than_limit = set()
for i in range(top + 1):
    for j in range(right + 1):
        dist_sum = sum(
            abs(i - coord_i) + abs(j - coord_j) 
                for (coord_i, coord_j), coord_id in coords_to_id.items())
        
        if dist_sum < LIMIT:
            coords_less_than_limit.add((i, j))
    

seen = set()
max_area = 0
for i in range(top + 1):
    for j in range(right + 1):
        if (i, j) in coords_less_than_limit and (i, j) not in seen:
            
            # expand point
            explored_points = 0
            stack = deque([(i, j)])
            while stack:
                i, j = stack.popleft()
                
                if (i, j) in seen:
                    continue
                
                seen.add((i, j))
                explored_points += 1
                
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if (ni, nj) in coords_less_than_limit and (ni, nj) not in seen:
                        stack.append((ni, nj))
            
            # update max area
            max_area = max(max_area, explored_points) 

print(f"Part Two: {max_area}")
