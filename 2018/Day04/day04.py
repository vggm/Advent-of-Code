from collections import defaultdict
from collections import Counter


with open("./test.txt", "r") as fr:
    lines = fr.readlines()
    

messages = []
for line in lines:
    line = line[1:] # remove '['
    datetime, message = line.split("] ")
    
    date, time = datetime.split(" ")
    hour, minute = list(map(int, time.split(":")))
    year, month, day = list(map(int, date.split("-")))
    
    message_type = message.split(" ")[1].strip() # [guard] id / [wakes] up / [falls] asleep
    
    messages.append((year, month, day, hour, minute, message_type))
    
messages.sort()


guards = {guard_id: defaultdict(list) for *_, guard_id in messages if guard_id.startswith("#")}

lst_grd = ""
for *_, minute, msg_type in messages:
    if msg_type.startswith("#"):
        lst_grd = msg_type
    
    elif msg_type == "asleep":
        guards[lst_grd]["asleep"].append(minute)
    
    else:
        guards[lst_grd]["up"].append(minute)
        

# ================= Part One ================= #

time_asleep = Counter()

for guard_id in guards.keys():
    asleeps = guards[guard_id]["asleep"]
    wakesup = guards[guard_id]["up"]
    
    total_diff = 0
    for m1, m2 in zip(asleeps, wakesup):
        total_diff += m2 - m1

    time_asleep[guard_id] = total_diff
    
guard_id_max_asleep, max_time_asleep = time_asleep.most_common(1)[0]
print(f"Max time asleep guard id is {guard_id_max_asleep} with {max_time_asleep} minutes asleep.")


asleeps = guards[guard_id_max_asleep]["asleep"]
wakesup = guards[guard_id_max_asleep]["up"]

minutes_asleep = Counter()
for m1, m2 in zip(asleeps, wakesup):
    minutes_asleep[minute] += 1

most_common_minute = minutes_asleep.most_common(1)[0][0]
print(f"Most common minute is {most_common_minute}\n")

print(f"Part One: {int(guard_id_max_asleep[1:]) * most_common_minute}")


# ================= Part Two ================= #

minutes_asleep = Counter()

for guard_id in guards.keys():
    asleeps = guards[guard_id]["asleep"]
    wakesup = guards[guard_id]["up"]
    
    for m1, m2 in zip(asleeps, wakesup):
        for minute in range(m1, m2):
            minutes_asleep[(int(guard_id[1:]), minute)] += 1

guard_id, minutes = minutes_asleep.most_common(1)[0][0]
print(f"Part Two: {guard_id * minutes}")
