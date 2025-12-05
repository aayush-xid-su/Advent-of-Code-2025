def solve():
    with open("day5input.txt") as f:
        sections = f.read().strip().split("\n\n")

    ranges = []
    for line in sections[0].splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    available_ids = [int(x) for x in sections[1].splitlines()]

    def is_fresh(ingredient_id):
        for start, end in ranges:
            if start <= ingredient_id <= end:
                return True
        return False

    count_fresh = sum(1 for n in available_ids if is_fresh(n))

    print("Fresh ingredient count:", count_fresh)


if __name__ == "__main__":
    solve()
