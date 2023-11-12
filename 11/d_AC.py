#a = []
#for i in range(10):
#    a.append(i)
#print(a)
#print(a[-2])
#a.pop()
#print(a)
#exit()


s = input()
ans = ["x","x"]
for i in range(len(s)):
    if ans[-1] == "B" and ans[-2] == "A" and s[i] == "C":
        ans.pop()
        ans.pop()
    else:
        ans.append(s[i])
print("".join(ans[2:]))