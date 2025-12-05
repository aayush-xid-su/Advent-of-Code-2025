def solve():
    with open("day5input.txt") as f:
        content = f.read().strip()

    ranges_section = content.split("\n\n")[0]

    ranges = []
    for line in ranges_section.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ranges.sort()

    merged = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))

    total_fresh = sum((end - start + 1) for start, end in merged)

    print("Total fresh ingredient IDs:", total_fresh)


if __name__ == "__main__":
    solve()
