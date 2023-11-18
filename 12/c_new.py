import collections
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
        rem.append(now)
        right += 1
        if right >= len(s):
            c = collections.Counter(rem)
            print(len(c.most_common()))
            exit()
    i += 1
c = collections.Counter(rem)
print(len(c.most_common()))

