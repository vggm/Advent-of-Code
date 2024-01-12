
import sys

POSSIBLE_MOVES = ((-1, 0), (1, 0), (0, -1), (0, 1))

def get_map(filename: str) -> list[str]:
  return open(filename).read().strip().split('\n')


def part_one(M: list[str]) -> int:
  init_pos = (0, 1)
  end_pos = (len(M)-1, len(M[0])-2)
  max_path = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
  
  def bt(step: int, curr: tuple[int, int], curr_path: set[tuple[int, int]]) -> None:
    
    if curr == end_pos:
      return
    
    i, j = curr
    for y, x in POSSIBLE_MOVES:
      ni, nj = i+y, j+x
      if 0 <= ni < len(M) and 0 <= nj < len(M[0]):
        if M[ni][nj] != '#'\
        and (ni, nj) not in curr_path\
        and ( M[ni][nj] == '.'
          or (M[ni][nj] == '>' and x != -1)
          or (M[ni][nj] == '<' and x != 1)
          or (M[ni][nj] == 'v' and y != -1)
          or (M[ni][nj] == '^' and y != 1))\
        and step+1 > max_path[ni][nj]:
          max_path[ni][nj] = step+1
          curr_path.add(curr)
          bt(step+1, (ni, nj), curr_path)
          curr_path.remove(curr)
  
  bt(0, init_pos, set())
  return max_path[end_pos[0]][end_pos[1]]
          

def main() -> None:
  sys.setrecursionlimit(9999)  # This line is required to not get RecursionError exception
  M = get_map('./input.txt')
  print(f'Part One: {part_one(M)}')


if __name__ == "__main__":
  main()
# end main