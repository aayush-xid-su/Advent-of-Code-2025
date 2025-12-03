def process_line(bank: str) -> int:
    batteries = []
    current_index = 0

    for i in range(11):

        end = len(bank) - 11 + i
        window = bank[current_index:end]

        index, first_max = max(
            enumerate(window),
            key=lambda x: x[1]
        )

        batteries.append(first_max)
        current_index = current_index + index + 1

    remaining = bank[current_index:]
    _, second_max = max(
        enumerate(remaining),
        key=lambda x: x[1]
    )

    batteries.append(second_max)

    return int("".join(batteries))


def process_file(filename: str) -> str:
    total = 0

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                total += process_line(line)

    return str(total)


if __name__ == "__main__":
    result = process_file("day3input.txt")
    print(result)
