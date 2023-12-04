from collections import deque
import math
s = input()

number = ["1","2","3","4","5","6","7","8","9","0"]

#print(s)

dic = {
    "a" : [],
    "b" : [],
    "c" : [],
    "d" : [],
    "e" : [],
    "f" : [],
    "g" : [],
    "h" : [],
    "i" : [],
    "j" : [],
    "k" : [],
    "l" : [],
    "m" : [],
    "n" : [],
    "o" : [],
    "p" : [],
    "q" : [],
    "r" : [],
    "s" : [],
    "t" : [],
    "u" : [],
    "v" : [],
    "w" : [],
    "x" : [],
    "y" : [],
    "z" : [],
}

q = deque([])
q.append(1)
n = 0
for i in range(len(s)):
    #print(s[i])
    #print(q)
    if s[i] in dic:
        if n != 0:
            q.append(n)
            #dic[s[i]].append(list(q))
            dic[s[i]].append(math.prod(list(q)))
            q.pop()
        else:
            #dic[s[i]].append(list(q))
            dic[s[i]].append(math.prod(list(q)))
        n = 0
        #print(dic[s[i]])
    elif s[i] == "(":
        if n != 0:
            q.append(n)
        else:
            q.append(1)
        n = 0
    elif s[i] in number:
        n = int(s[i]) + n * 10
    elif s[i] == ")":
        q.pop()
#print(*dic)
print("a",sum(dic["a"]))
print("b",sum(dic["b"]))
print("c",sum(dic["c"]))
print("d",sum(dic["d"]))
print("e",sum(dic["e"]))
print("f",sum(dic["f"]))
print("g",sum(dic["g"]))
print("h",sum(dic["h"]))
print("i",sum(dic["i"]))
print("j",sum(dic["j"]))
print("k",sum(dic["k"]))
print("l",sum(dic["l"]))
print("m",sum(dic["m"]))
print("n",sum(dic["n"]))
print("o",sum(dic["o"]))
print("p",sum(dic["p"]))
print("q",sum(dic["q"]))
print("r",sum(dic["r"]))
print("s",sum(dic["s"]))
print("t",sum(dic["t"]))
print("u",sum(dic["u"]))
print("v",sum(dic["v"]))
print("w",sum(dic["w"]))
print("x",sum(dic["x"]))
print("y",sum(dic["y"]))
print("z",sum(dic["z"]))