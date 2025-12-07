from typing import List, Set, Tuple

def read_grid(filename: str = "day7input.txt") -> List[str]:
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    return lines

def find_start(grid: List[str]) -> Tuple[int, int]:
    for r, row in enumerate(grid):
        c = row.find('S')
        if c != -1:
            return r, c
    raise ValueError("Start 'S' not found in grid")

def count_splits(grid: List[str]) -> int:
    rows = len(grid)
    if rows == 0:
        return 0
    cols = max(len(row) for row in grid)
    grid = [row.ljust(cols) for row in grid]

    start_r, start_c = find_start(grid)

    active: Set[int] = set()
    if start_r + 1 < rows:
        active.add(start_c)

    splits = 0

    for r in range(start_r + 1, rows):
        if not active:
            break

        next_active: Set[int] = set()
        for c in active:
            if c < 0 or c >= cols:
                continue
            ch = grid[r][c]
            if ch == '^':
                splits += 1
                left = c - 1
                right = c + 1
                if 0 <= left < cols:
                    next_active.add(left)
                if 0 <= right < cols:
                    next_active.add(right)
            else:
                next_active.add(c)

        active = next_active

    return splits

if __name__ == "__main__":
    grid = read_grid("day7input.txt")
    splits = count_splits(grid)
    print("Beam split count:", splits)
