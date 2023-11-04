n = int(input())
s = input()

for i in range(n):
    if i == 0:
        continue
    if s[i] == "a":
        if s[i-1] == "b":
            print('Yes')
            exit()
    elif s[i] == "b":
        if s[i-1] == "a":
            print("Yes")
            exit()
print('No')