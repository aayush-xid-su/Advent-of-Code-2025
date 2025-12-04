DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

def count_adjacent(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    return count


def solve():
    with open("day4input.txt", "r") as f:
        grid = [list(line.strip()) for line in f]

    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    accessible_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adj = count_adjacent(grid, r, c)
                if adj < 4:
                    result[r][c] = 'x'
                    accessible_count += 1

    print("Accessible rolls:", accessible_count)
    print()
    for row in result:
        print("".join(row))


if __name__ == "__main__":
    solve()
