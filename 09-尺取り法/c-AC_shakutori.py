n , m = map(int,input().split())

a = list(map(int,input().split()))
a = sorted(a)
#a.append(99999999999999)
ans = 0
right = 0
for i in range(len(a)):
    #ma = 0
    #right = i
    while right < len(a) and (a[right] - a[i]) < m:
        #ma += 1
        right += 1
    ans = max(right-i,ans)
print(ans)