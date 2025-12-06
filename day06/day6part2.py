import operator
from functools import reduce

with open('day6input.txt', 'r') as f:
    mat = []
    for line in f.readlines():
        mat.append(list(line.strip('\n')))
n = len(mat)
m = len(mat[0])
for _ in range(m - len(mat[-1])):
    mat[-1].append(' ')
result2 = 0
k = 0
while k < m:
    op = mat[-1][k]
    k2 = k + 1
    while k2 < m and mat[-1][k2] == ' ':
        k2 += 1
    temp = 0 if op == '+' else 1
    for j in range(k, k2):
        colstr = ''.join(mat[i][j] for i in range(n-1))
        if not colstr.strip():
            continue
        num = int(colstr)
        if op == '+':
            temp += num
        else:
            temp *= num
    result2 += temp
    k = k2
print(result2)