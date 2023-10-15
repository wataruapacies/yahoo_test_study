in_str = input().split()

n = int(in_str[0])
t = in_str[1]

s = [input() for i in range(n)]

#print(n,t)

#print(s)

m = len(t)

ans =[]
next_flag = False
for i in range(n):
    if m == len(s[i]):
        if t == s[i]:
            ans.append(i+1)
        else:
            for j in range(m):
                #if j == 0 or j == m-1:
                #    continue
                if t[:j] == s[i][:j] and t[j+1:] == s[i][j+1:]:
                    ans.append(i+1)
                    next_flag = True
                    break
    elif m == len(s[i])-1:
        for j in range(len(s[i])):
            #if j == len(s[i]):
            #    continue
            new = s[i][:j] + s[i][j+1:]
            if t == new:
                ans.append(i+1)
                break
    elif m == len(s[i])+1:
        for j in range(len(t)):
            #if j == len(s[i]):
            #    continue
            new = t[:j] + t[j+1:]
            if new == s[i]:
                ans.append(i+1)
                break
    if next_flag:
        next_flag = False
        continue
print(len(ans))
print(*ans)