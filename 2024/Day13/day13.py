import sys
import pyperclip as cp
from sympy import symbols, Eq, solve
from sympy.core.numbers import Integer


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n\n")


A_TOKEN, B_TOKEN = 3, 1


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 
 
def get_parameters(query: str) -> tuple[int, int, int, int, int, int]:
  bta, btb, prize = query.split("\n")
  (ax, ay), (bx, by), (px, py) = bta[10:].split(", "), btb[10:].split(", "), prize[7:].split(", ")
  ax, ay = ax[2:], ay[2:]
  bx, by = bx[2:], by[2:]
  px, py = px[2:], py[2:]
  return int(ax), int(ay), int(bx), int(by), int(px), int(py)


def part_one(queries: list[str], offset=0) -> int:
  
  total_answer = 0
  for query in queries:
    ax, ay, bx, by, px, py = get_parameters(query)
    
    px, py = px + offset, py + offset
    
    x, y = symbols('x y')
    
    eq1 = Eq(ax*x + bx*y, px)
    eq2 = Eq(ay*x + by*y, py)
    
    solution = solve((eq1, eq2), (x, y))
    
    a, b = solution[x], solution[y]
    if type(a) == Integer and type(b) is Integer:
      total_answer += a * A_TOKEN + b * B_TOKEN
    
  return total_answer


def part_two(queries: list[str]) -> int:
  return part_one(queries, offset=10000000000000)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()
  
  input = read_file(sys.argv[1])
  pr("Part One:", part_one(input))
  pr("Part Two:", part_two(input))
  