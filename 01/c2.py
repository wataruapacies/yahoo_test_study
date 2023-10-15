n , m = map(int,input().split())
a = list(map(int,input().split()))

s = [list(input()) for i in range(n)]

#print('a = ',a)

#print('s = ',s)

point = [0] * n
not_include = [[] for _ in range(n)]
#print('not_include[] = ',not_include)

for i in range(n):
    point[i] += 1+i
    for j in range(m):
        if s[i][j] == 'o':
            point[i] += a[j]
        else:
            not_include[i].append(a[j])
    not_include[i] = sorted(not_include[i],reverse=True)

maxpoint = max(point)

#print('maxpoint = ',maxpoint)
#print('point[] = ',point)
#print('not_include[] = ',not_include)

for i in range(n):
    ans = 0
    if point[i] == maxpoint:
        print(ans) 
    else:
        for j in range(len(not_include[i])):
            point[i] += not_include[i][j]
            ans += 1
            if point[i] >= maxpoint:
                print(ans)
                break