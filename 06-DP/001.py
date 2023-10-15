n = int(input())

h = list(map(int,input().split()))

ans1 = [h[0]] * n
ans2 = [h[0]] * n
ans = ans1
#print(ans)
for i in range(n):
    if i == 0:
        continue
    if i == 1 :
        ans1[i] = ans1[0] + abs(h[i] - h[0])
        ans2[i] = ans2[0] + abs(h[i] - h[0])
        if ans1[i] > ans2[i]:
            ans[i] = ans2[i]
        else:
            ans[i] = ans1[i]
        continue
    ans1[i] = ans[i-1] + abs(h[i] - h[i-1])
    ans2[i] = ans[i-2] + abs(h[i] - h[i-2])
    if ans1[i] > ans2[i]:
        ans[i] = ans2[i]
    else:
        ans[i] = ans1[i]
print(ans[n-1]-ans[0])