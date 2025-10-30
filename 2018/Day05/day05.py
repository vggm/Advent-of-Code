with open("./input.txt", "r") as fr:
    lines = fr.readlines()

sentence = lines[0].strip()

jump = ord("a") - ord("A")

def do_react(sen: str) -> int:

    last_size = 0
    while last_size != len(sen):
        last_size = len(sen)
        
        i = 0
        while i < len(sen) - 1:
            
            if abs(ord(sen[i]) - ord(sen[i+1])) == jump:
                # skip both chars
                sen = sen[:i] + sen[i+2:]
            
            else:
                i += 1
    
    return len(sen)
    
print(f"Part One: {do_react(sentence)}")

chars = set(sentence)
can_remove_all: list[str] = []
for c in chars:
    if chr(ord(c) - jump) in chars:
        can_remove_all.append(c)

print(f"Part Two: {
    min(  do_react(sentence\
            .replace(unit, "")\
            .replace(chr(ord(unit) - jump), "")) 
                for unit in can_remove_all)}")