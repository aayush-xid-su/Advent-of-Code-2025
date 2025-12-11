import re
from z3 import Optimize, Int, sat

with open("day10input.txt", "r") as f:
    inp = f.read().strip()

def solve(target, buttons):
    steps = 0
    n = len(target)
    states = set()
    states.add((0,) * n)

    while True:
        steps += 1
        new_states = set()

        for state in states:
            for button in buttons:
                new_states.add(tuple(
                    (state[i] + (i in button)) % 2 for i in range(n)
                ))

        if target in new_states:
            return steps

        states = new_states


def solvej(buttons, joltages):
    n = len(buttons)
    s = Optimize()

    p = [Int(f"p{i}") for i in range(n)]

    for i in range(n):
        s.add(p[i] >= 0)

    for t in range(len(joltages)):
        s.add(sum(p[i] for i in range(n) if t in buttons[i]) == joltages[t])

    presses = Int("presses")
    s.add(presses == sum(p))

    s.minimize(presses)

    if s.check() == sat:
        m = s.model()
        return m[presses].as_long()

    return None


part1 = part2 = 0

for raw in inp.splitlines():
    line = raw.strip()
    if not line:
        continue

    m = re.match(r'\[(.*?)\]\s+(.*?)\s+\{(.*?)\}', line)
    if not m:
        print("Skipping invalid line:", line)
        continue

    target_raw, buttons_raw, jolt_raw = m.groups()

    target = tuple(c == '#' for c in target_raw)

    buttons = []
    for bstr in buttons_raw.split():
        nums = bstr[1:-1]
        if nums == "":
            buttons.append(set())
        else:
            buttons.append(set(map(int, nums.split(","))))

    joltages = tuple(map(int, jolt_raw.split(",")))

    part1 += solve(target, buttons)
    part2 += solvej(buttons, joltages)

print("Part 1 Answer", part1)
print("Part 2 Answer:", part2)
