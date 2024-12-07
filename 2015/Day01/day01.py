import pyperclip as cp
import sys

if len(sys.argv) < 2:
    print("Usage: python3 day01.py input.in")
    print("Must include the input file!")
    exit()

def pr(s: str, ans: int):
    print(s, ans)
    cp.copy(ans)

in1 = open(sys.argv[1]).read().strip()

def mapper(p: str) -> int:
    return 1 if p == "(" else -1

p1 = sum(x for x in map(mapper, in1))

lvl = 0
for i, p in enumerate(in1, start=1):
    lvl += mapper(p)
    if lvl == -1:
        p2 = i
        break

pr("Part One:", p1)
pr("Part Two:", p2)
