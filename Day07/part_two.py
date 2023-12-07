import functools
from collections import Counter

labels = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
label2rank = {l: i for i, l in enumerate(labels)}

file = open('input.txt').read().strip().split('\n')
hands = [(h.split()[0], int(h.split()[1])) for h in file]
total_of_hands = len(file)

types = [[], [], [], [], [], [], []]


def which_type(co: Counter) -> int:
  mc, m = co.most_common()[0]
  mc2, m2 = co.most_common()[1] if len(co) > 1 else (0, 0)
  j_exists = 'J' in co

  if j_exists:
    if mc == 'J':
      m += m2
    else:
      m += co['J']

  if m == 5:
    return 0  # five of a kind
  elif m == 4:
    return 1  # four of a kind
  elif m == 3:
    if j_exists:
      if len(co) == 3:
        return 2
      return 3
    if len(co) == 2:
      return 2  # full house
    return 3  # three of kind
  elif m == 2:
    if j_exists:
      if len(co) == 4:
        return 4
      return 5
    if len(co) == 3:
      return 4  # two pair
    return 5  # one pair
  return 6  # high card


def compare_str(h1: str, h2: str) -> int:
  if label2rank[h1[0]] > label2rank[h2[0]]:
    return 1
  elif label2rank[h1[0]] < label2rank[h2[0]]:
    return -1
  else:
    return compare_str(h1[1:], h2[1:])


for h, b in hands:
  c = Counter(h)
  i = which_type(c)
  types[i].append((h, b))

ans = 0
i = total_of_hands
for t in types:
  t = sorted(t, key=functools.cmp_to_key(lambda h1, h2: compare_str(h1[0], h2[0])))
  for h, b in t:
    ans += b * i
    i -= 1

print(ans)
