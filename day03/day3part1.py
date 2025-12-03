def process(input_str: str) -> str:
    total = 0

    for bank in input_str.splitlines():
        truncated = bank[:-1]

        index, first_max = max(
            enumerate(truncated),
            key=lambda x: x[1]
        )

        rest = bank[index + 1:]
        second_max = max(rest)

        total += int(first_max + second_max)

    return str(total)


def main():
    with open("day3input.txt", "r", encoding="utf-8") as f:
        data = f.read().strip()

    result = process(data)
    print(result)


if __name__ == "__main__":
    main()
