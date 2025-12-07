from functools import lru_cache

def read_grid(filename="day7input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    if not lines:
        return []
    width = max(len(line) for line in lines)
    return [line.ljust(width) for line in lines]

def find_start(grid):
    for r, row in enumerate(grid):
        c = row.find("S")
        if c != -1:
            return r, c
    raise ValueError("Start 'S' not found")

def count_timelines(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    start_r, start_c = find_start(grid)
    start_row = start_r + 1

    @lru_cache(maxsize=None)
    def timelines_from(r, c):
        if c < 0 or c >= cols:
            return 1
        rr = r
        while rr < rows and grid[rr][c] != '^':
            rr += 1
        if rr >= rows:
            return 1
        left_count = timelines_from(rr + 1, c - 1)
        right_count = timelines_from(rr + 1, c + 1)
        return left_count + right_count

    if start_row >= rows:
        return 1
    return timelines_from(start_row, start_c)

if __name__ == "__main__":
    grid = read_grid("day7input.txt")
    total = count_timelines(grid)
    print("Total timelines:", total)
