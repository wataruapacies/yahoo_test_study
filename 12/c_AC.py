import collections
import itertools

N = int(input())
S = input()

d = collections.defaultdict(int)
for c, g in itertools.groupby(S):
    d[c] = max(d[c], len(list(g)))
print(sum(d.values()))
# 模範解答
