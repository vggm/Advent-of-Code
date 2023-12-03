
total_sum = 0

SPELLED_DIGITS = {
  'one':    '1', 
  'two':    '2', 
  'three':  '3', 
  'four':   '4', 
  'five':   '5', 
  'six':    '6', 
  'seven':  '7', 
  'eight':  '8', 
  'nine':   '9'
}

def exists_in_spelled_digits ( sub_str: str, reverse=False ) -> bool:
  
  if not reverse:
    for digit in SPELLED_DIGITS.keys():
      if digit.startswith(sub_str):
        return True
  
  else:
    for digit in SPELLED_DIGITS.keys():
      if digit.endswith(sub_str):
        return True
  
  return False

def calculate_value ( line: str ) -> int:
  start, end = 0, len(line)-1
  first, last = False, False
  start_num, end_num = '', ''
  found = False
  
  sub_start, sub_end = '', ''
  last_start, last_end = start, end
  while start <= end and not found:
    c_start, c_end = line[start], line[end]
    
    if not first:
      if c_start.isdigit():
        start_num = c_start
        first = True
      else:
        sub_start += c_start
        if not exists_in_spelled_digits(sub_start):
          start = last_start + 1
          last_start = start
          sub_start = ''
        else:
          if len(sub_start) == 1:
            last_start = start
          if SPELLED_DIGITS.get(sub_start) is not None:
            start_num = SPELLED_DIGITS[sub_start]
            first = True
          else:
            start += 1
          
    if not last:
      if c_end.isdigit():
        end_num = c_end
        last = True
      else:
        sub_end = c_end + sub_end
        if not exists_in_spelled_digits(sub_end, True):
          end = last_end - 1
          last_end = end
          sub_end = ''
        else:
          if len(sub_end) == 1:
            last_end = end
          if SPELLED_DIGITS.get(sub_end) is not None:
            end_num = SPELLED_DIGITS[sub_end]
            last = True
          else:
            end -= 1
    
    if first and last: 
      found = True
  
  answer = start_num + end_num
  return int(answer)
  
  
def read_file ( filename: str ) -> None:
  global total_sum
  with open(filename) as file:
    line = file.readline().removesuffix('\n')
    while line != '':
      total_sum += calculate_value( line )
      line = file.readline().removesuffix('\n')
      

if __name__ == '__main__':
  read_file( './Day01/input2.txt' )
  print( 'Total Sum:', total_sum )