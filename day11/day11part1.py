def count_paths(graph, start, end, memo):
    if start in memo:
        return memo[start]

    if start == end:
        return 1

    total = 0
    for nxt in graph.get(start, []):
        total += count_paths(graph, nxt, end, memo)

    memo[start] = total
    return total


def parse_input(lines):
    graph = {}
    for line in lines:
        src, rest = line.split(":")
        targets = rest.strip().split()
        graph[src.strip()] = targets
    return graph

with open("day11input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

graph = parse_input(lines)
answer = count_paths(graph, "you", "out", {})

print("Number of paths from you → out:", answer)
