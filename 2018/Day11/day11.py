SERIAL_NUMBER = 2694

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
                
