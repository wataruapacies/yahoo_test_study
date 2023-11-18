n = int(input())
a = list(map(int,input().split()))

b = sorted(a,reverse=True)
i = 1
ans = 0
while True:
    if b[i] != b[0]:
        ans = b[i]
        break
    i += 1
print(ans)