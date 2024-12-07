import pyperclip as cp
import sys

if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    print("Must include the input file!")
    exit()

def pr(s: str, ans: int):
    print(s, ans)
    cp.copy(ans)

L = open(sys.argv[1]).read().strip().split()

p1 = p2 = 0
for l, w, h in map(lambda l: list(map(int, l.split('x'))), L):
    mmin = min(l*w, w*h, h*l)
    m1, m2, _ = sorted([l, w, h])
    p1 += 2*(l*w + w*h + h*l) + mmin
    p2 += m1*2 + m2*2 + l*w*h

pr("Part One:", p1)
pr("Part Two:", p2)
