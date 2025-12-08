import heapq
import math
import sys
from itertools import combinations

K = 1000 


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_sizes(self):
        for i in range(len(self.parent)):
            self.parent[i] = self.find(i)
        counts = {}
        for p in self.parent:
            counts[p] = counts.get(p, 0) + 1
        return list(counts.values())


def read_points(filename="day8input.txt"):
    pts = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                raise ValueError(f"Bad line: {line!r}")
            x, y, z = map(int, parts)
            pts.append((x, y, z))
    return pts


def squared_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


def k_smallest_pairs(points, k=K):
    n = len(points)
    if n < 2:
        return []

    heap = []
    push = heapq.heappush
    pop = heapq.heappop

    for (i, j) in combinations(range(n), 2):
        d = squared_dist(points[i], points[j])
        if len(heap) < k:
            push(heap, (-d, i, j))
        else:
            if d < -heap[0][0]:
                pop(heap)
                push(heap, (-d, i, j))
    result = [(-negd, i, j) for (negd, i, j) in heap]
    result.sort(key=lambda t: t[0])
    return result


def main():
    points = read_points("day8input.txt")
    n = len(points)
    if n == 0:
        print("No points found in day8input.txt")
        return

    total_pairs = n * (n - 1) // 2
    k = min(K, total_pairs)

    print(f"Read {n} points, selecting {k} smallest pairs...", file=sys.stderr)

    smallest = k_smallest_pairs(points, k)

    dsu = DSU(n)

    applied = 0
    for dist, i, j in smallest:
        dsu.union(i, j)
        applied += 1
        if applied >= k:
            break

    sizes = dsu.component_sizes()
    sizes.sort(reverse=True)
    top3 = sizes[:3] + [1, 1]
    product = top3[0] * top3[1] * top3[2]
    print(product)


if __name__ == "__main__":
    main()