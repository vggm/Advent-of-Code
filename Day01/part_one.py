
total_sum = 0

def calculate_value ( line: str ) -> int:
  start, end = 0, len(line)-1
  found = False
  first, last = False, False
  while start <= end and not found:
    if not first:
      if line[start].isdigit():
        first = True
      else:
        start += 1
    
    if not last:
      if line[end].isdigit():
        last = True
      else:
        end -= 1
    
    if first and last: 
      found = True
  
  answer = line[start] + line[end]
  return int(answer)
  
  
def read_file ( filename: str ) -> None:
  global total_sum
  with open(filename) as file:
    line = file.readline().removesuffix('\n')
    while line != '':
      total_sum += calculate_value( line )
      line = file.readline().removesuffix('\n')
      

if __name__ == '__main__':
  read_file( './input1.txt' )
  print( 'Total Sum:', total_sum )