
def get_differences(numbers: list[int]) -> list[list[int]]:
  diff = []
  differences, nums = [numbers.copy()], numbers.copy()
  while not all(d == 0 for d in nums):
    diff.clear()
    for i in range(len(nums)-1):
      diff.append(nums[i+1]-nums[i])
    differences.append(diff.copy())
    nums = diff.copy()
  return differences


def prediction(numbers: list[int]) -> int:
  differences = get_differences(numbers)
  differences[-1].append(0)
  for i in range(len(differences)-2, -1, -1):
    last = differences[i][-1]
    below = differences[i+1][-1]
    differences[i].append(last + below)
  return differences[0][-1]


def extrapolate_backward(numbers: list[int]) -> int:
  differences = get_differences(numbers)
  differences[-1].insert(0, 0)
  for i in range(len(differences)-2, -1, -1):
    first = differences[i][0]
    below = differences[i+1][0]
    differences[i].insert(0, first - below)
  return differences[0][0]


if __name__ == '__main__':
  file = open('input.txt').read().strip()
  lines = file.split('\n')

  ans = sum(prediction(list(map(int, line.split())))
             for line in lines)

  print('Part 1:', ans)

  ans = sum(extrapolate_backward(list(map(int, line.split())))
            for line in lines)

  print('Part 2:', ans)
