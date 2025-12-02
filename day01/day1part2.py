"""
    Day 1 part 2
    Dail starts at 50
    Dail goes from 0 - 99
    Password is # times it pointing to 0 after each rotation
    
"""
dir_list = []
amount_list = []

with open("day1.txt", "r") as file:
    for line in file:
        line = line.strip()

        dir_list.append(line[0])
        amount_list.append(int(line[1:]))

current_position = 50
ayush = 0

def hits_through_zero(current_position, distance, direction):
    # normalize the starting position into 0-99
    s = current_position % 100
    first_zero_hit_at = (((100 - s) if direction == "R" else s)) or 100 # if left evals to 0, it will be 100
    if distance < first_zero_hit_at:
        return 0
    return 1 + (distance - first_zero_hit_at) // 100 # always 1 hit from first_zero_hit_at + rest

for i in range(len(dir_list)):
    direction = dir_list[i]
    distance = amount_list[i]
    ayush += hits_through_zero(current_position, distance, direction)
    if direction == "R":
        current_position = (current_position + distance) % 100
    if direction == "L":
        current_position = (current_position - distance) % 100


print(ayush)

# Time complexity: O(n)
# ayush is used as a easter egg