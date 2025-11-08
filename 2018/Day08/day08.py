
with open("./input.txt", "r") as fr:
    lines = fr.read().strip()

data = list(map(int, lines.split(" ")))


# ========== Part One ========== #

def explore_metadata(pos: int) -> tuple[int, int]:
    num_childs, num_metadata_entries = data[pos], data[pos + 1]
    
    total_sum = 0
    nxt_pos = pos + 2
    for _ in range(num_childs):
        parcial_sum, nxt_pos = explore_metadata(nxt_pos)
        total_sum += parcial_sum
    
    total_sum += sum(
        data[i] 
        for i in range(nxt_pos, nxt_pos + num_metadata_entries))
    return total_sum, nxt_pos + num_metadata_entries
    
total_sum, nxt_pos = explore_metadata(0)
print(f"Part One: {total_sum}")


# ========== Part Two ========== #

def explore_metadata(pos: int) -> tuple[int, int]:
    num_childs, num_metadata_entries = data[pos], data[pos + 1]
    nxt_pos = pos + 2
    
    has_childs = num_childs > 0
    
    if has_childs: 
        
        index: dict[int, int] = {}
        for i in range(1, num_childs + 1):
            parcial_sum, nxt_pos = explore_metadata(nxt_pos)
            index[i] = parcial_sum
            
        total_sum = sum(
            index[data[i]] 
            for i in range(nxt_pos, nxt_pos + num_metadata_entries) 
                if data[i] in index)
    
    else:
        total_sum = sum(
            data[i] 
            for i in range(nxt_pos, nxt_pos + num_metadata_entries))
        
    return total_sum, nxt_pos + num_metadata_entries
    
total_sum, nxt_pos = explore_metadata(0)
print(f"Part Two: {total_sum}")
