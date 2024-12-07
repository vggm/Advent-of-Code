import pyperclip as cp
import sys

if len(sys.argv) < 2:
    print("Usage: python3 day01.py input.in")
    print("Must include the input file!")
    exit()

def pr(s: str, ans: int):
    print(s, ans)
    cp.copy(ans)

in1 = open(sys.argv[1]).read().strip().split()

def mapper(p: str) -> int:
    return 1 if p == "(" else -1

p1 = sum(x for row in in1 for x in map(mapper, row))

pr("Part One:", p1)
