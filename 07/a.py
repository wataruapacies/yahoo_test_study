import itertools

n , m = map(int,input().split())

a = list(map(int,input().split()))

b = [[0,0] for _ in range(m)]

#print(b)
mm = 2 * m - n

#print(mm)

for _ in range(mm):
    a.append(0)

#for i in range(n):
#print(a)

aa = list(itertools.permutations(a))

#print(len(aa))
ans = []
#print(aa[0])
for i in range(len(aa)):
    #print(aa[i])
    s = 0
    for j in range(len(aa[i])):
        if j == int(len(aa[i]))/2:
            break
        s = s + (aa[i][2*j]+aa[i][2*j+1])**2
    ans.append(s)

#print(*ans)
print(min(ans))
