

cards = {}


def calculate_copies(card_id: int, cache={}) -> int:
  if cache.get(card_id) is not None:
    return cache[card_id]

  own_numbers, winning_numbers = cards[card_id].split('|')
  winning_numbers = set(winning_numbers.split())

  matches = sum(1 if num in winning_numbers else 0 for num in own_numbers.split())

  cache[card_id] = matches
  return matches


def calculate_nodes(card_id: int, memo={}) -> int:
  if memo.get(card_id) is not None:
    return memo[card_id]

  copies = calculate_copies(card_id)
  if copies == 0:
    memo[card_id] = 1
    return 1

  result = sum(calculate_nodes(card_i)
               for card_i in range(card_id + 1, card_id + copies + 1)) + 1

  memo[card_id] = result
  return result


def cards_copies() -> int:
  total_copies = 0
  for card_id in cards.keys():
    total_copies += calculate_nodes(card_id)

  return total_copies


def read_file(filename: str) -> None:
  global cards
  with open(filename) as file:
    card = file.readline().removesuffix('\n')
    while card != '':
      card_name, numbers = card.split(':')
      _, card_id = card_name.split()
      cards[int(card_id)] = numbers
      card = file.readline().removesuffix('\n')


if __name__ == '__main__':
  read_file('./test.txt')
  answer = cards_copies()
  print('Answer:', answer)
