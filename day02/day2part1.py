def is_invalid_id(value: int) -> bool:
    value_str = str(value)
    mid = len(value_str) // 2
    left = value_str[:mid]
    right = value_str[mid:]
    return left == right


def part_one(ranges: list[str]):
    invalids = []

    for r in ranges:
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            if is_invalid_id(i):
                invalids.append(i)

    print(sum(invalids))


# Read file
with open("day2.txt", "r", encoding="utf-8") as f:
    lines = f.read().strip()

# Run function
part_one(lines.split(","))
