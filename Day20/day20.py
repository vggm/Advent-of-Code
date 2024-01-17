
from collections import deque
import math

LOW_PULSE = False
HIGH_PULSE = True
Pulse = bool


class Module:
  def __init__(self, name: str):
    self.name = name
    self.pulse_status = LOW_PULSE
    self.pulses_sent = 0
  
  def send_pulse(self, pulse: Pulse, name: str) -> None:
    self.pulse_status = pulse
    self.pulses_sent += 1
    
class FlipFlop(Module):
  def __init__(self, name: str):
    super().__init__(name)
  
  def send_pulse(self, pulse: Pulse, name: str) -> None:
    if pulse == HIGH_PULSE: # if high, do nothing
      return
    self.pulse_status = not self.pulse_status
    
class Conjuction(Module):
  def __init__(self, name: str):
    super().__init__(name)
    self.inputs_pulses = []
    self.names_to_index = {}
    self.inputs_connected = 0
    
  def set_inputs(self, inputs: int):
    self.inputs_pulses = [LOW_PULSE for _ in range(inputs)]
  
  def send_pulse(self, pulse: Pulse, name: str) -> None:
    
    if self.names_to_index.get(name) is None:
      self.names_to_index[name] = self.inputs_connected
      self.inputs_connected += 1
    
    inp = self.names_to_index[name]
    self.inputs_pulses[inp] = pulse
    if all(self.inputs_pulses):
      self.pulse_status = LOW_PULSE
    else:
      self.pulse_status = HIGH_PULSE


lines = open('./input.txt').read().splitlines()

adjacency : dict[str, set] = {}
modules : dict[str, Module] = {}

flipflops : dict[str, FlipFlop] = {}
conjuntions : dict[str, Conjuction] = {}

for module, connections in list(map(lambda s: s.split(' -> '), lines)):
  module_name = module
  module_type = module[0]
  if module_type in ['%', '&']:
    module_name = module[1:]
    if module_type == '&':
      module = Conjuction(module_name)
      conjuntions[module_name] = module
    else:
      module = FlipFlop(module_name)
      flipflops[module_name] = module
  else:
    module = Module(module_name)
  modules[module_name] = module
  adjacency[module_name] = set(list(connections.split(', ')))
  
# find conjuntions inputs
for name, conj in conjuntions.items():
  cont = 0
  for input in modules:
    if name in adjacency[input]:
      cont += 1
  conj.set_inputs(cont)

pulses_needed = { # based on input
  'vt': 0,
  'sk': 0, 
  'xc': 0,
  'kk': 0,
}

low = 0
high = 0
for i in range(10000):
  # print(f'Iteration {i+1}:')
  # print('button -low-> broadcaster')
  if i < 1000: # part one
    low += 1 # button low pulse
  stack = deque([modules['broadcaster']])
  
  while stack:
    module = stack.popleft()
    pulse_to_send = module.pulse_status
    
    for conn in adjacency[module.name]:
      
      if modules.get(conn) is None:
        modules[conn] = Module(conn)
        adjacency[conn] = set()
      
      m_adj = modules[conn]
      m_adj.send_pulse(pulse_to_send, module.name)
      
      if module.name in pulses_needed.keys() and pulse_to_send == HIGH_PULSE:
        if pulses_needed[module.name] == 0:
          pulses_needed[module.name] = i+1
      
      if i < 1000: # part one
        if pulse_to_send == LOW_PULSE:
          low += 1
        else:
          high += 1
      
      # pulse = 'low' if pulse_to_send == LOW_PULSE else 'high'
      # print(f'{module.name} -{pulse}-> {m_adj.name}')
      
      if type(m_adj) is FlipFlop and pulse_to_send == HIGH_PULSE:
        continue
        
      stack.append(m_adj)
    
  # print()

ans = high * low
print(f'Low: {low} / High: {high}')
print(f'Part 1: {ans}')

print(f'\n{pulses_needed}')
print(f'Part 2: {math.lcm(*pulses_needed.values())}')
