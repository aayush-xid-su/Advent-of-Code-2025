def parse_presents(lines, i):
    presents = []

    while i < len(lines):
        line = lines[i].strip()

        if "x" in line and ":" in line and line[0].isdigit():
            break

        if line.endswith(":"):
            present_id = int(line[:-1])
            i += 1

            pattern_lines = []
            while i < len(lines):
                ln = lines[i].strip()
                if ln == "" or ln.endswith(":"):
                    break
                pattern_lines.append(ln)
                i += 1

            hash_count = sum(row.count("#") for row in pattern_lines)
            presents.append((present_id, hash_count))
        else:
            i += 1

    return presents, i


def parse_dimension_lines(lines, i):
    dim_lines = []

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        if "x" in line and ":" in line:
            left, right = line.split(":")
            x, y = map(int, left.split("x"))
            nums = list(map(int, right.strip().split()))
            dim_lines.append(((x, y), nums))

        i += 1

    return dim_lines


def process(input_text):
    lines = input_text.splitlines()

    presents, idx = parse_presents(lines, 0)
    dim_lines = parse_dimension_lines(lines, idx)
    present_weights = [count for (_id, count) in presents]

    result = 0

    for (x, y), present_counts in dim_lines:
        total_weight = 0

        for idx, num in enumerate(present_counts):
            total_weight += present_weights[idx] * num

        if x * y > total_weight:
            result += 1

    return str(result)

if __name__ == "__main__":
    with open("day12input.txt", "r", encoding="utf-8") as f:
        text = f.read()

    print(process(text))
