n , q = map(int,input().split())
s = input()
l = []
r = []
ans = []
check = []
cnt = 0
check.append(cnt)
for i in range(n):
    if i == 0:
        continue
    if s[i-1] == s[i]:
        cnt += 1
    check.append(cnt)


for _ in range(q):
    li , ri = map(int,input().split())
    l.append(li)
    r.append(ri)
    
    ans.append(check[ri-1]-check[li-1])
for i in range(len(ans)):
    print(ans[i])