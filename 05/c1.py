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
    err = 0
    if abs(m-len(s[i])) > 1:
        continue
    if len(s[i]) > len(t):
        for j in range(len(t)):
            if t[j] == s[i][j] and err == 0:
                pass
            elif t[j] == s[i][j+1]:
                err = 1
            else:
                err = 2
                break
        if err < 2:
            ans.append(i+1)
    elif len(s[i]) < len(t):
        for j in range(len(s[i])):
            if s[i][j] == t[j] and err == 0:
                pass
            elif s[i][j] == t[j+1]:
                err = 1
            else:
                err = 2
                break
        if err < 2:
            ans.append(i+1)
    elif len(s[i]) == len(t):
        for j in range(len(t)):
            if s[i][j] == t[j]:
                pass
            else:
                err = err + 1
        if err < 2:
            ans.append(i+1)
print(len(ans))
print(*ans)
        