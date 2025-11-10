
with open("./test.txt", "r") as fr:
    lines = fr.readlines()
    
for line in lines:
    line = line.strip()
    position, velocity = line[:17], line[18:]
    print(f"{position}-{velocity}")

