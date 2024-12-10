import sys
import pyperclip as cp
from collections import defaultdict, deque


def read_file(filename: str) -> str:
  return open(filename).read().strip()


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)


def get_id():
  i = 0
  while True:
    yield i
    i += 1


FREE_SPACE = -1
def part_one(input: list[str]) -> int:
  
  cnt = get_id()
  usage: list[int] = []
  for i, n in enumerate(input):
    data = next(cnt) if i % 2 == 0 else FREE_SPACE
    usage.extend([data] * int(n))
    
  checksum = 0
  l, r = 0, len(usage)-1
  while l <= r:
    
    if usage[l] != FREE_SPACE:
      checksum += usage[l] * l
      l += 1
    
    elif usage[r] == FREE_SPACE:
      r -= 1
    
    else:
      checksum += usage[r] * l
      l, r = l+1, r-1
  
  return checksum


def part_two(input: list[str]) -> int:
  
  free_id = get_id()
  block_id = get_id()
  ids: list[int] = []
  free_mem: list[int] = []
  id_cnt: dict[int, int] = {}
  mem_pos: dict[int, int] = {}
  fre_pos: dict[int, int] = {}
  for i, n in enumerate(input):
    if i % 2 == 0:
      memid = next(block_id)
      ids.append(memid)
      id_cnt[memid] = int(n)
      mem_pos[memid] = i
    
    else:
      if n != '0':
        ids.append(FREE_SPACE)
        free_mem.append(int(n))
        fre_pos[next(free_id)] = i
  
  free_mem_occ = [[] for _ in free_mem]
  # print(ids)
  # print(id_cnt)
  # print(free_mem)
  # print(free_mem_occ)
  
  id_cnt_items = list(id_cnt.items())
  for block_index in range(len(id_cnt_items)-1, -1, -1):  
    block, size = id_cnt_items[block_index]
    
    for i, free_size in enumerate(free_mem):
      if fre_pos[i] > mem_pos[block]: # space after block
        break
      
      if free_size >= size:
        free_mem[i] -= size
        free_mem_occ[i].append(block)
        break
  
  # print(free_mem)
  # print(free_mem_occ)
  
  final_mem = ""
  free_index = 0
  final_mem_ls = []
  seen: set[int] = set()
  for block_id in ids:
    if block_id == -1:
      for block_id in free_mem_occ[free_index]:
        seen.add(block_id)
        final_mem_ls.extend([block_id]*id_cnt[block_id])
        final_mem += f"{block_id}" * id_cnt[block_id]
      final_mem_ls.extend([-1] * free_mem[free_index])
      final_mem += "." * free_mem[free_index]
      free_index += 1
      continue
    
    if block_id not in seen:
      final_mem += f"{block_id}" * id_cnt[block_id]
      final_mem_ls.extend([block_id]*id_cnt[block_id])
      
    else:
      final_mem += "." * id_cnt[block_id]
      final_mem_ls.extend([-1] * id_cnt[block_id])
  
  # print(final_mem_ls)
  # print(final_mem)
  
  checksum = 0
  for pos, block_id in enumerate(final_mem_ls):
    checksum += block_id * pos if block_id != -1 else 0
    
  return checksum


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input = read_file(sys.argv[1])
  pr("Part One:", part_one(input))
  pr("Part Two:", part_two(input))
  