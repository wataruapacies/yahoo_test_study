n , m = map(int,input().split())

a = list(map(int,input().split()))
a = sorted(a)
#print(a)
ans = [0] * n
ans_start = [0] * n
ans_num = [1] * n
ma = 1

arry = []
point = []
num = 0
#for i in range(len(a)):
#    if i > 0:
#        if a[i-1] == a[i]:
#            num += 1
#        else:
#            arry.append(num)
#            point.append(a[i-1])
#            num = 0
            
        
        
for i in range(len(a)):
    if i > 0:
        if a[i-1] == a[i]:
            continue
    for j in range(len(a)-i):
        if j == 0:
            continue
        if (a[i+j] - a[i]) < m:
            #print(i,j)
            ans_num[i] = ans_num[i] + 1
            if ma < ans_num[i]:
                ma = ans_num[i]
        else:
            break

print(ma)
#print(*ans_num)