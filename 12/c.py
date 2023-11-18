n = int(input())
s = list(input())

count = 0
right = 0
rem = []
i = 0
while i < len(s):
    if right < i:
        right = i
    while s[i] == s[right]:
        #ma += 1
        now = "".join(s[i:right+1])
        if now not in rem:
            count += 1
#            print(now)
            rem.append(now)
        right += 1
        if right >= len(s):
            print(count)
            exit()
    i += 1
print(count)