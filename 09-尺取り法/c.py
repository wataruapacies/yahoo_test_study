n , m = map(int,input().split())

a = list(map(int,input().split()))
#print(a)
ans = [0] * n
ans_start = [0] * n
ans_num = [0] * n
ma = 0
for i in range(len(a)):
    for j in range(len(a)):
        #if j <= i:
        #    continue
        if (a[j] - a[i]) < m and (a[j] - a[i]) >= 0:
            #print(i,j)
            ans_num[i] = ans_num[i] + 1
            if ma < ans_num[i]:
                ma = ans_num[i]
            ans[i] = a[j] - a[i]
            ans_start[i] = a[i]
        #else:
        #    break

print(ma)
#print(*ans_num)