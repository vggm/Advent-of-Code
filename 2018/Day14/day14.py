
N_RECIPIES = int(input("Num of recipies: "))

def list_of_digits(n: int) -> int:
  if n < 10:
    return [n]
  
  return list_of_digits(n // 10) + [n % 10]


# ============ Part One ============ #

i, j = 0, 1
recipies = [3, 7]
while len(recipies) < N_RECIPIES + 10:
  i = (i + recipies[i] + 1) % len(recipies)
  j = (j + recipies[j] + 1) % len(recipies)

  new_recipies = list_of_digits(recipies[i] + recipies[j])
  
  for new_recipie in new_recipies:
    recipies.append(new_recipie)


print(f"Part One: {\
  ''.join(list(map(str, recipies[N_RECIPIES:N_RECIPIES+10])))}")


# ============ Part Two ============ #

def same_list(list1: list[int], list2: list[int]) -> bool:
  for n1, n2 in zip(list1, list2):
    if n1 != n2:
      return False
  
  return True
  

target = list_of_digits(N_RECIPIES)
num_len = len(target)


ans = -1

i, j = 0, 1
found = False
recipies = [3, 7]
while not found:
  i = (i + recipies[i] + 1) % len(recipies)
  j = (j + recipies[j] + 1) % len(recipies)

  new_recipies = list_of_digits(recipies[i] + recipies[j])
  
  for new_recipie in new_recipies:
    recipies.append(new_recipie)
  
  if len(recipies) > num_len:
    if same_list(recipies[-num_len:], target):
      ans = len(recipies) - num_len
      found = True
  
  if not found and len(new_recipies) == 2 and (len(recipies) - 1) > num_len:
    if same_list(recipies[-num_len-1:-1], target):
      ans = len(recipies) - num_len - 1
      found = True
      
print(f"Part Two: {ans}")
