
from collections import defaultdict


class Graph:
  def __init__(self) -> None:
    self.vertex = set()
    self.matrix = defaultdict(set)
    
  def add_edge(self, v1: str, v2: str) -> None:
    if v1 not in self.vertex:
      self.vertex.add(v1)
    if v2 not in self.vertex:
      self.vertex.add(v2)
    
    self.matrix[v1].add(v2)
    self.matrix[v2].add(v1)
  
  def remove_edge(self, v1: str, v2: str) -> None:
    if not self.vertex.issuperset([v1, v2]):
      return
    
    self.matrix[v1].remove(v2)
    self.matrix[v2].remove(v1)
    
  def print_mat(self) -> None:
    print('Matrix -- ')
    for k, v in self.matrix.items():
      print(f'{k}: {v}')
    print('---')  


def get_graph(filename: str) -> Graph:
  graph = Graph()
  with open(filename) as f:
    for row in f.read().strip().split('\n'):
      node, adjs = row.split(': ')
      for adj in adjs.split():
        graph.add_edge(node, adj)
  
  return graph


if __name__ == '__main__':
  G = get_graph('./test')
  G.print_mat()
  