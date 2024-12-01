
def worth_points(card: str):
  card_name, numbers = card.split(':')
  own_numbers, winning_numbers = numbers.split('|')
  winning_numbers = set(winning_numbers.split())

  worth_value = 0
  for number in own_numbers.split():
    if number in winning_numbers:
      worth_value = 1 if not worth_value else worth_value*2

  return worth_value


def get_total_sum(filename: str) -> int:
  total_sum = 0
  with open(filename) as file:
    card = file.readline().removesuffix('\n')
    while card != '':
      total_sum += worth_points(card)
      card = file.readline().removesuffix('\n')
  return total_sum


if __name__ == '__main__':
    answer = get_total_sum('./input.txt')
    print('Answer:', answer)
