

def get_strings(filename: str) -> list[str]:
  return open(filename).read().strip().split(',')


def character_hash(c: str, current: int) -> int:
  return (current + ord(c)) * 17 % 256 


def hash(string: str) -> int:
  current = 0
  for c in string:
    current = character_hash(c, current)
  return current


def part_one(strings: list[str]) -> int:
  return sum(hash(s) for s in strings)


def part_two(strings: list[str]) -> int:
  boxes = [{} for _ in range(256)]
  for s in strings:
    if '=' in s: # add/update
      label, number = s.split('=')
      box = hash(label)
      boxes[box][label] = int(number)
    else: # remove
      label = s[:-1]
      box = hash(label)
      if boxes[box].get(label) is not None:
        boxes[box].pop(label)
  
  return sum((i+1) * slot * focal 
             for i, box in enumerate(boxes) 
             for slot, (_, focal) in enumerate(box.items(), start=1))    


if __name__ == '__main__':
  string_list = get_strings('./input.txt')
  print(f'Part one: {part_one(string_list)}')
  print(f'Part two: {part_two(string_list)}')
  # print(hash('rn'))
  