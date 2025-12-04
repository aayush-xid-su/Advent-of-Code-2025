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
            if grid[nr][nc] == "@":
                count += 1
    return count


def solve():
    with open("day4input.txt", "r") as f:
        grid = [list(line.strip()) for line in f]

    rows, cols = len(grid), len(grid[0])

    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    adj = count_adjacent(grid, r, c)
                    if adj < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = "."
        total_removed += len(to_remove)

    print("Total rolls removed:", total_removed)


if __name__ == "__main__":
    solve()
