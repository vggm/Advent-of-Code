
with open("./input.txt") as fr:
  IDs = fr.read().strip().split(",")
  
IDs = list(
        map(
          lambda x: 
            list(
              map(
                int, 
                x.split("-"))), 
          IDs))


# =========== Part One =========== #

def num_of_digits(n: int) -> int:
  if n < 10:
    return 1
  
  return num_of_digits(n // 10) + 1

cnt = 0
for first_id, last_id in IDs:
  for num in range(first_id, last_id + 1):
    num_len = num_of_digits(num)
    if num_len % 2 == 1:
      continue
    
    mid = num_len // 2
    num_str = str(num)
    if num_str[:mid] == num_str[mid:]:
      cnt += num

print(f"Part One: {cnt}")


# =========== Part Two =========== #

cnt = 0
for first_id, last_id in IDs:
  for num in range(first_id, last_id + 1):
    
    num_str = str(num)
    num_len = len(num_str)
    for size in range(1, num_len):
      if num_len % size != 0:
        continue
      
      cmp = num_str[:size]
      for i in range(1, num_len // size):
        value = num_str[size*i:size*i+size]
        if value != cmp:
          break
      
      else:
        cnt += num
        break
      
print(f"Part Two: {cnt}")
