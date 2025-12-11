import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
edges = collections.defaultdict(set)
for line in inp.splitlines():
    source, targets_str = line.split(': ')
    for target in targets_str.split(' '):
        edges[source].add(target)

ordered = []
visited = set()
def dfs(node):
    visited.add(node)
    for target in edges[node]:
        if target not in visited:
            dfs(target)
    ordered.append(node)
dfs('you')

def count_paths(source, final_target):
    paths = collections.defaultdict(int)
    paths[source] = 1
    for node in reversed(ordered):
        for target in edges[node]:
            paths[target] += paths[node]
    return paths[final_target]
print("part 1 answer:" ,count_paths('you', 'out'))

ordered = []
visited = set()
dfs('svr')

print("part 2 answer:",
    (count_paths('svr', 'fft') * 
     count_paths('fft', 'dac') * 
     count_paths('dac', 'out')) +
    (count_paths('svr', 'dac') * 
     count_paths('dac', 'fft') * 
     count_paths('fft', 'out')))