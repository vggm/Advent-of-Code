import math
import sys
from typing import Callable
import pyperclip as cp


def read_file(filename: str) -> list[str]:
  return open(filename).read().strip().split("\n")


def pr(s: str, ans: int):
  print(s, ans)
  cp.copy(ans)
 

class CPU:
  def __init__(self, A=0, B=0, C=0, find_target=False):
    self.A: int = A
    self.B: int = B
    self.C: int = C
    
    self.operand: int = -1
    self.pointer: int = 0
    
    self.output: list[str] = []
    
    self.inc_2: bool = True
    
    self.ops: dict[int, Callable] = {
      0: self._adv,
      1: self._bxl,
      2: self._bst,
      3: self._jnz,
      4: self._bxc,
      5: self._out,
      6: self._bdv,
      7: self._cdv
    }
    
    self.find_target: bool = find_target
    self.target: list[int] = []
    
    
  def run(self, program: list[int]) -> str:
    self.target = program[:]
    while self.pointer < len(program):
      self.inc_2 = True
      
      opcode = program[self.pointer]
      self.operand = program[self.pointer+1]
      
      self._make_op(opcode)
      
      if self.inc_2:
        self.pointer += 2
    
    return ",".join(map(str, self.output))
  
  def _make_op(self, opcode:int):
    self.ops[opcode]()
    
  def _calculate_combo(self) -> int:
    if self.operand < 4:
      return self.operand
    
    val = -1
    match self.operand:
      case 4:
        val = self.A
      case 5:
        val = self.B
      case 6:
        val = self.C
      case _:
        pass
    
    return val

  def _adv(self):
    self.A //= (2 ** self._calculate_combo())
  
  def _bxl(self):
    self.B ^= self.operand
  
  def _bst(self):
    self.B = self._calculate_combo() % 8
  
  def _jnz(self):
    if self.A != 0:
      self.pointer = self.operand
      self.inc_2 = False
  
  def _bxc(self):
    self.B ^= self.C
  
  def _out(self):
    res = self._calculate_combo() % 8
    if self.find_target and res != self.target[len(self.output)]:
      self.pointer = len(self.target) + 10
      return
    
    self.output.append(res)
    
    if len(self.output) == len(self.target):
      self.pointer = len(self.target) + 10
    print(",".join(map(str, self.output)), end='\r')

  def _bdv(self):
    self.B = self.A // (2 ** self._calculate_combo())
  
  def _cdv(self):
    self.C = self.A // (2 ** self._calculate_combo())


def get_params(file: list[str]) -> tuple[list[int], list[int]]:
  registers = []
  for i in range(3):
    registers.append(int(file[i].split(": ")[1]))

  program = list(map(int, file[4][9:].split(",")))

  return registers, program


def part_one(file_input: list[str]) -> int:
  registers, program = get_params(file_input)
  
  cpu = CPU(*registers)
  return cpu.run(program)
  
  
def part_two(file_input: list[str]) -> int:
  _, program = get_params(file_input)
  str_program = ",".join(map(str,program))
  
  ans = 117440
  cpu = CPU(A=ans, find_target=True)
  while cpu.run(program) != str_program:
    ans += 1
    cpu = CPU(A=ans, find_target=True)
  
  return ans


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Usage: python3 dayXX.py input.in")
    exit()

  file_input = read_file(sys.argv[1])
  pr("Part One:", part_one(file_input))
  # pr("Part Two:", part_two(file_input))
  