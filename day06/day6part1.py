import re
from functools import reduce
from operator import mul

def read_grid(filename="day6input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    width = max(len(line) for line in lines) if lines else 0
    grid = [line.ljust(width) for line in lines]
    return grid

def find_problem_ranges(grid):
    cols = list(zip(*grid)) if grid else []
    blank_indices = [i for i, col in enumerate(cols) if all(ch == " " for ch in col)]
    ranges = []
    start = 0
    for b in blank_indices:
        if b > start:
            ranges.append((start, b))
        start = b + 1
    width = len(cols)
    if start < width:
        ranges.append((start, width))
    return ranges

def extract_numbers_from_problem(problem_rows, op_row_index):
    numbers = []
    for row in problem_rows[:op_row_index]:
        m = re.search(r"\d+", row)
        if m:
            numbers.append(int(m.group()))
        else:
            continue
    return numbers

def solve(filename="day6input.txt"):
    grid = read_grid(filename)
    if not grid:
        print("Grand total: 0")
        return

    problem_ranges = find_problem_ranges(grid)
    grand_total = 0

    for left, right in problem_ranges:
        problem_rows = [row[left:right] for row in grid]

        op = None
        op_row = None
        for r in range(len(problem_rows) - 1, -1, -1):
            row = problem_rows[r]
            if '+' in row or '*' in row:
                op = '+' if '+' in row else '*'
                op_row = r
                break
        if op is None:
            continue

        numbers = extract_numbers_from_problem(problem_rows, op_row)
        if not numbers:
            continue

        if op == '+':
            result = sum(numbers)
        else:
            result = reduce(mul, numbers, 1)

        grand_total += result

    print("Grand total:", grand_total)

if __name__ == "__main__":
    solve("day6input.txt")
