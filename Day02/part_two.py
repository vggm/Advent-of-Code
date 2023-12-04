
sum_of_the_power_IDs = 0

class Game:
  def __init__(self, row: str) -> None:
    game_record = row.split(':')
    
    self.id = int(game_record[0].split()[1])
    self.records = game_record[1].split(';')
    self.minimum_values = {
      'red': 0, 'green': 0, 'blue': 0
    }
    self.power_of_set = 1
    self._calculate_minimum()
    self._calculate_power_of_set()
    
  def _calculate_minimum(self):
    for set_of_cubes in self.records:
      for reveal in set_of_cubes.split(','):
        count, color = reveal.split()
        if int(count) > self.minimum_values[color]:
          self.minimum_values[color] = int(count)
  
  def _calculate_power_of_set(self):
    for minimum in self.minimum_values.values():
      self.power_of_set *= minimum


def read_file ( filename: str ) -> None:
  global sum_of_the_power_IDs
  with open(filename) as file:
    row = file.readline().removesuffix('\n')
    while row != '':
      game = Game(row)
      sum_of_the_power_IDs += game.power_of_set
      row = file.readline().removesuffix('\n')


if __name__ == '__main__':
  read_file('./input2.txt')
  print('Total sum:', sum_of_the_power_IDs)