import re

with open("./test.txt", "r") as fr:
    lines = fr.readlines()

for line in lines:
    steps_found = re.findall(r"\s[A-Z]{1}\s", line)
    
