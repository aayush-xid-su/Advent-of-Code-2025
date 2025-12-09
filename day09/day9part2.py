import itertools

with open("day9input.txt", "r") as f:
    inp = f.read().strip()

pts = []
for line in inp.splitlines():
    pts.append(tuple(map(int, line.split(','))))

N = len(pts)

cols = sorted(set(c for c, _ in pts))
rows = sorted(set(r for _, r in pts))
C, R = len(cols), len(rows)

col_map = {c: i for i, c in enumerate(cols)}
row_map = {r: i for i, r in enumerate(rows)}

def compress_pt(pt):
    return (col_map[pt[0]], row_map[pt[1]])

grid = [[' '] * 250 for _ in range(250)]

pts_loop = pts + [pts[0]]

for pt1, pt2 in itertools.pairwise(pts_loop):
    c1, r1 = compress_pt(pt1)
    c2, r2 = compress_pt(pt2)

    if c1 == c2:
        for r in range(min(r1, r2), max(r1, r2) + 1):
            grid[c1][r] = '#'
    else:
        for c in range(min(c1, c2), max(c1, c2) + 1):
            grid[c][r1] = '#'

stack = [(0, 0), (249, 0)]
while stack:
    c, r = stack.pop()
    if not (0 <= c < 250 and 0 <= r < 250):
        continue
    if grid[c][r] != ' ':
        continue
    grid[c][r] = 'X'
    stack.append((c-1, r))
    stack.append((c+1, r))
    stack.append((c, r-1))
    stack.append((c, r+1))

part2 = 0

for i, pt1 in enumerate(pts):
    for j in range(i + 1, N):
        pt2 = pts[j]
        c1, r1 = compress_pt(pt1)
        c2, r2 = compress_pt(pt2)

        is_ok = True
        for c in range(min(c1, c2), max(c1, c2) + 1):
            for r in range(min(r1, r2), max(r1, r2) + 1):
                if grid[c][r] == 'X':
                    is_ok = False
                    break
            if not is_ok:
                break

        if is_ok:
            area = (abs(pt1[0] - pt2[0]) + 1) * (abs(pt1[1] - pt2[1]) + 1)
            part2 = max(part2, area)

print("Part 2:", part2)
