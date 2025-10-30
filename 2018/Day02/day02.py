from collections import Counter

with open("./input.txt", "r") as fr:
    lines = fr.readlines()

checksum: list[int] = [0, 0]
for line in lines:
    cnt = Counter(line)
    val = set(cnt.values())

    for i, num in enumerate([2, 3]):
        if num in val:
            checksum[i] += 1

print(f"Part One: {checksum[0] * checksum[1]}")


def diff_str(str1: str, str2: str) -> int:
    idx = -1
    found = False

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found:
                return -1
            idx = i
            found = True

    return idx


for i, str1 in enumerate(lines):
    for str2 in lines[i + 1 :]:
        pos = diff_str(str1, str2)
        if pos == -1:
            continue

        print(f"Part Two: {str1[:pos] + str1[pos + 1 :]}")
