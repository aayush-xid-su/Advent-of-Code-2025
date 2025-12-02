def is_invalid_id_part2(value: int) -> bool:
    """
    Return True if 'value' consists of some digit-sequence repeated >= 2 times.
    """
    s = str(value)
    n = len(s)

    for k in range(1, n // 2 + 1):
        if n % k == 0:
            chunk = s[:k]
            if chunk * (n // k) == s:
                return True

    return False


def solve_part_two(ranges: list[str]) -> int:
    invalid_ids = []

    for r in ranges:
        start, end = map(int, r.split('-'))
        for v in range(start, end + 1):
            if is_invalid_id_part2(v):
                invalid_ids.append(v)

    return sum(invalid_ids)


#input file 
with open("day2.txt", "r", encoding="utf-8") as f:
    line = f.read().strip()

ranges = line.split(",")

answer = solve_part_two(ranges)
print(answer)
