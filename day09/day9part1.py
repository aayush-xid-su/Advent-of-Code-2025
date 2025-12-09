with open("day9input.txt", "r") as f:
    inp = f.read().strip()

pts = []
for line in inp.splitlines():
    pts.append(tuple(map(int, line.split(','))))

N = len(pts)

part1 = 0
for i, pt1 in enumerate(pts):
    for j in range(i + 1, N):
        pt2 = pts[j]
        area = (abs(pt1[0] - pt2[0]) + 1) * (abs(pt1[1] - pt2[1]) + 1)
        part1 = max(part1, area)

print("Part 1:", part1)
