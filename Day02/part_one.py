
CONFIGURATION = {
  'red': 12,
  'green': 13,
  'blue': 14
}

sum_of_IDs = 0

class Game:
  def __init__(self, row: str) -> None:
    game_record = row.split(':')
    
    self.id = int(game_record[0].split()[1])
    self.records = game_record[1].split(';')
    self.valid = True
    self._verify()
    
  def _verify(self):
    for set_of_cubes in self.records:
      for reveal in set_of_cubes.split(','):
        count, color = reveal.split()
        if int(count) > CONFIGURATION[color]:
          self.valid = False
          return


def read_file ( filename: str ) -> None:
  global sum_of_IDs
  with open(filename) as file:
    row = file.readline().removesuffix('\n')
    while row != '':
      game = Game(row)
      if game.valid:
        sum_of_IDs += game.id
      row = file.readline().removesuffix('\n')


if __name__ == '__main__':
  read_file('./input1.txt')
  print('Total sum:', sum_of_IDs)