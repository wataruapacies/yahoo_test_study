# https://atcoder.jp/contests/abc325/tasks/abc325_c
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
 
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
 
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 
 
    def same(self,a,b):
        return self.leader(a) == self.leader(b)
 
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])
 
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r!=[]]
    
if __name__ == '__main__':
    h , w = map(int,input().split())
    s = []
    sens = []
    not_sens = 0
    #uni_f = UnionFind(h*w+1)
    for i in range(h):
        s.append(list(input()))
        for j in range(w):
            if s[i][j] == "#":
                sens.append([i,j])
    #            for ki in range(2):
    #                print('i-ki',i-ki)
    #                for kj in range(2):
    #                    print('j-kj',j-kj)
    #                    if i-ki<0 or j-kj<0:
    #                        continue
    #                    if kj==0 and ki==0:
    #                        continue
    #                    if s[i-ki][j-kj] == "#":
    #                        uni_f.merge(i*j+1,(i-ki)*(j-kj)+1)
    #        else:
    #            not_sens = not_sens + 1
                        
    #s = [list(input()) for l in range(h)]

    #print(s)
    #print(s[1][3])

    
    #for i in range(h):
    #    for j in range(w):
    #        if s[i][j] == "#":
    #            sens.append([i,j])
    #print(sens[1][1])
    if len(sens) == 0:
        print("0")
        exit()
    uni_f = UnionFind(len(sens)+1)
    #print(len(sens))
    friend = [[] for _ in range(len(sens))]
    for i in range(len(sens)):
        for j in range(len(sens)):
            if i <= j:
                continue
            if max(abs(sens[i][0]-sens[j][0]),abs(sens[i][1]-sens[j][1])) == 1:
                uni_f.merge(i+1,j+1)
        #print(uni_f.groups())
    #print('not_sens',not_sens)
    print(len(uni_f.groups())-1)