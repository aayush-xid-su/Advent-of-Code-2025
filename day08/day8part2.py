import heapq
from itertools import combinations


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def read_points(filename="day8input.txt"):
    pts = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                x, y, z = map(int, line.strip().split(","))
                pts.append((x, y, z))
    return pts


def squared_dist(a, b):
    return ((a[0] - b[0]) ** 2 +
            (a[1] - b[1]) ** 2 +
            (a[2] - b[2]) ** 2)


def main():
    pts = read_points("day8input.txt")
    n = len(pts)
    dsu = DSU(n)

    edges = []
    for i, j in combinations(range(n), 2):
        d = squared_dist(pts[i], pts[j])
        edges.append((d, i, j))

    edges.sort(key=lambda e: e[0])

    for d, i, j in edges:
        if dsu.union(i, j):
            if dsu.components == 1:
                xi = pts[i][0]
                xj = pts[j][0]
                print(xi * xj)
                return


if __name__ == "__main__":
    main()
