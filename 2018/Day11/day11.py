from tqdm import tqdm


SERIAL_NUMBER = 2694


# ================== Part One ================== #

def calculate_cell_value(x: int, y: int, serial=SERIAL_NUMBER) -> int:
    rack_id = x + 10
    power_lvl = rack_id * y
    
    cell_value = (power_lvl + serial) * rack_id
    cell_value = (cell_value // 100) % 10 - 5 
    
    return cell_value


# Tests
# print(calculate_cell_value(3, 5, 8))
# print(calculate_cell_value(122, 79, 57))
# print(calculate_cell_value(217, 196, 39))
# print(calculate_cell_value(101, 153, 71))


MATRIX_SIZE = 300
matrix = [[0 for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

for y in range(1, MATRIX_SIZE + 1):
    for x in range(1, MATRIX_SIZE + 1):
        i, j = y-1, x-1
        matrix[i][j] = calculate_cell_value(x, y)

idx_max = (1, 1)
max_value = sum(matrix[i][j] for j in range(3) for i in range(3))
for i in range(1, MATRIX_SIZE-1):
    for j in range(1, MATRIX_SIZE-1):   
        cell_value = sum(matrix[ii][jj] for jj in range(j-1, j+2) for ii in range(i-1, i+2))
        if cell_value > max_value:
            idx_max = (j, i)
            max_value = cell_value

x, y = idx_max
print(f"Part One: {x},{y}")
                

# ================== Part Two ================== #

max_size = 1
idx_max = (1, 1)
max_value = -9999999999
for size in tqdm(range(1, MATRIX_SIZE + 1), desc="Part Two"):
    
    block_value = sum(matrix[i][j] for j in range(size) for i in range(size)) 
    for i in range(MATRIX_SIZE - size + 1):
        
        if i > 0: # skip first iteration
            old_sum = sum(matrix[i-1][jj] for jj in range(size))
            new_sum = sum(matrix[i+size-1][jj] for jj in range(size))
            
            block_value += new_sum - old_sum
            
        last_first_block_value = block_value        
        for j in range(MATRIX_SIZE - size + 1):
            
            if j > 0: # skip first iteration
                old_sum = sum(matrix[ii][j-1] for ii in range(i, i + size))
                new_sum = sum(matrix[ii][j+size-1] for ii in range(i, i + size))
                
                block_value += new_sum - old_sum
               
            if block_value > max_value:
                idx_max = (j+1, i+1)
                max_size = size
                max_value = block_value
        
        block_value = last_first_block_value
        
        
x, y = idx_max
print(f"Part Two: {x},{y},{max_size} - Max value: {max_value}")
