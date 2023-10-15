n, m = map(int,input().split())

a = list(map(int,input().split()))

#print(a)

maru_batu = [0] * n

for i in range(m):
    maru_batu[a[i]-1] = 1

ans = [0] * n
pre = 0
for i in reversed(range(n)):
    if maru_batu[i] == 1:
        pre = 0
    else:
        pre += 1
        ans [i] = pre
#print(ans)

for i in range(n):
    print(ans[i])