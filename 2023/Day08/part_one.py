
F = open('input.txt').read().strip()
L = F.split('\n')
M = L[0]
N = {
  l.split(' = ')[0]: (l.split(' = ')[1].split(', ')[0].removeprefix('('),
                      l.split(' = ')[1].split(', ')[1].removesuffix(')'))
                        for l in L[2:]
}

source = 'AAA'
target = 'ZZZ'

cnt = 0
curr = source
found = False
while curr != target:
  m = M[cnt % len(M)]
  curr = N[curr][0 if m == 'L' else 1]
  cnt += 1

print(cnt)
