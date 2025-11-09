from glob import glob
import sys


class Node:
    def __init__(self, prv=None, nxt=None, data=0):
        self.prv: Node | None = prv
        self.nxt: Node | None = nxt
        self.data: int = data


class CircularLinkedList:
    def __init__(self):
        first_node: Node = Node(data=0)
        second_node: Node = Node(data=2)
        thirst_node: Node = Node(data=1)
        
        self.head = second_node
        self.head.nxt = thirst_node
        self.head.prv = first_node
        
        first_node.nxt = self.head
        first_node.prv = thirst_node
        
        thirst_node.prv = self.head
        thirst_node.nxt = first_node
    
    def insert_node(self, value: int):
        new_node = Node(data=value)
        
        new_node.nxt = self.head.nxt
        self.head.nxt.prv = new_node
        new_node.prv = self.head
        self.head.nxt = new_node
        
        self.head = self.head.nxt
    
    def remove_node(self) -> int:
        data = self.get_data()
        
        self.head.prv.nxt = self.head.nxt
        self.head.nxt.prv = self.head.prv
        self.head = self.head.nxt
        
        return data
    
    def show(self):
        actual_data = self.get_data()
        print(f"{actual_data} ", end="")
        
        curr = self.head.nxt
        while curr.data != actual_data:
            print(f"{curr.data} ", end="")
            curr = curr.nxt
        print()
    
    def forward(self) -> int:
        self.head = self.head.nxt
        return self.get_data()
    
    def backward(self) -> int:
        self.head = self.head.prv
        return self.get_data()
    
    def get_data(self) -> int:
        return self.head.data


# ============ Part One Function ============ #

def part_one(num_players: int, last_marble: int) -> int:
    score_players = [0] * (num_players + 1)

    # curr = 1

    marble = 3
    # game = [0, 2, 1]
    game = CircularLinkedList()

    player = 3
    while marble < last_marble:
        
        if marble % 23 != 0:
            # new_curr = curr + 2
            
            # if new_curr > len(game):
            #     new_curr %= len(game)
            
            # game.insert(new_curr, marble)
            
            game.forward()
            game.insert_node(marble)
        
        else:
            # new_curr = (curr - 7) % len(game)
            # players_points[player] += marble + game.pop(new_curr)

            for _ in range(7):
                game.backward()
            
            score_players[player] += marble + game.remove_node()
            
        marble += 1
        # curr = new_curr
        player = (player + 1) % num_players

    return max(score_players) 


# ============ Tests ============ #

print("### Running Tests ###")

test_success = 0
for idx, file in enumerate(glob("test*.txt"), start=1):
    with open(file, "r") as fr:
        line = fr.read().strip()
    
    words = line.split(" ")
    num_players, last_marble, expected = int(words[0]), int(words[6]), int(words[-1])
    
    test_passed = part_one(num_players=num_players, last_marble=last_marble) == expected
    test_success += test_passed
    
    print(f" - Test {idx}: {"Success!" if test_passed else "Fail"}")

print(f"Tests Passed: {test_success}/{idx}")


# ============ Part One ============ #

if test_success != idx:
    sys.exit(1)

with open("./input.txt", "r") as fr:
    line = fr.read().strip()

words = line.split(" ")
num_players, last_marble = int(words[0]), int(words[6])

print(f"\nPart One: {part_one(num_players=num_players, last_marble=last_marble)}")


# ============ Part Two ============ #

print(f"Part Two: {part_one(num_players=num_players, last_marble=last_marble*100)}")
    