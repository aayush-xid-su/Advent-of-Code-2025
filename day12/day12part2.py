def parse_input(data: str):
    sections = data.strip().split("\n\n")

    presents = []
    for block in sections:
        if ":" not in block:
            continue
        lines = block.splitlines()
        if lines[0].endswith(":") and lines[0][0].isdigit():
            idx = int(lines[0][:-1])
            shape_lines = lines[1:]
            hash_count = sum(row.count("#") for row in shape_lines)
            presents.append((idx, hash_count))
        else:
            break

    region_lines = sections[-1].strip().split("\n")
    regions = []
    for line in region_lines:
        size_part, counts_part = line.split(": ")
        w, h = map(int, size_part.lower().split("x"))
        counts = list(map(int, counts_part.split()))
        regions.append(((w, h), counts))

    return presents, regions


def solve_part1(data: str) -> int:
    presents, regions = parse_input(data)

    total = 0
    for (w, h), counts in regions:
        area = w * h

        required_area = 0
        for (index, shape_hashes), qty in zip(presents, counts):
            required_area += shape_hashes * qty

        if area > required_area:
            total += 1

    return total


def solve_part2(_data: str) -> str:
    raise NotImplementedError("Part 2 is already completed.")

print("You go look for a ladder; only 23 stars to go.\n")
print("if you are seeing this than you have came long way bro just have a sit and take some coffee bcz ")
print("At this point, all that is left is for you to admire your Advent calendar. Enjoy your holiday\n \n")
def main():
    with open("day12input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    # Part 1
    part1_answer = solve_part1(data)
    # print("Part 1:", part1_answer)

    # Part 2
    try:
        part2_answer = solve_part2(data)
        # print("Part 2:", part2_answer)
    except NotImplementedError as e:
        print("Part 2: TODO -", e)


if __name__ == "__main__":
    main()
