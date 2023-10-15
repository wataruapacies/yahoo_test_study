n = int(input())
s = [input() for i in range(n)]

#print('s = ',s)

count = [0] * n

for i in range(n):
    for j in range(len(s[i])):
        if s[i][j] =='o':
            count[i] += 1
ans = []
for k in reversed(range(n)):
    for i in range(n):
        if count[i] == k:
            ans.append(i+1)
print(*ans)