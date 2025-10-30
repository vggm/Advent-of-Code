import itertools as it

with open("./input.txt", "r") as fr:
    lines = fr.readlines()

nums = list(map(int, lines))
print(f"Part One: {sum(nums)}")

seen: set[int] = set()

curr_sum = 0
for num in it.cycle(nums):
    curr_sum += num
    if curr_sum in seen:
        print(f"Part Two: {curr_sum}")
        exit(1)
    seen.add(curr_sum)

print("Part Two: Not Found!")
