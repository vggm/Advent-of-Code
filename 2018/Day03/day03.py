with open("./input.txt", "r") as fr:
    lines = fr.readlines()

height = 0
width = 0

claims: list[tuple[str, int, int, int, int]] = []
for line in lines:
    id, other = line.split(" @ ")
    pos, size = other.split(": ")
    lf, tp = pos.split(",")
    w, h = size.split("x")

    height = max(height, int(tp) + int(h) + 1)
    width = max(width, int(lf) + int(w) + 1)

    claims.append((id, int(lf), int(tp), int(w), int(h)))

m = [[0 for _ in range(width)] for _ in range(height)]

for id, lf, tp, w, h in claims:
    for i in range(tp, tp + h):
        for j in range(lf, lf + w):
            m[i][j] += 1

cnt = sum(1 for row in m for val in row if val >= 2)

print(f"Part One: {cnt}")

for id, lf, tp, w, h in claims:
    overlap = False
    for i in range(tp, tp + h):
        if overlap:
            break
        for j in range(lf, lf + w):
            if m[i][j] > 1:
                overlap = True
                break

    if not overlap:
        break

print(f"Part Two: {id.removeprefix('#')}")
