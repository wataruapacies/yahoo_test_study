# https://atcoder.jp/contests/abc231/tasks/abc231_d
# https://qiita.com/sano192/items/be8f3e8df5bf2f394755#d---kaibunsyo
# https://qiita.com/sano192/items/2b2656202b767109387e#d---neighbors


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
    n , m = map(int,input().split())

    a = []
    b = []

    #辺の数
    hen = [0]*(n+1)
    
    for _ in range(m):
        ai , bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    
    
    uni_f = UnionFind(n+1)
    
    for i in range(m):
        hen[a[i]] += 1
        hen[b[i]] += 1
        
        if hen[a[i]] > 2 or hen[b[i]] > 2:
            print('No')
            exit()
            
        if uni_f.same(a[i],b[i]):
            print('No')
            exit()
        else:
            uni_f.merge(a[i],b[i])
        
    print('Yes')
    
    #グループ全体の確認
    #print(uni_f.groups())
    
    #根の確認
    #print(uni_f.leader(3))
    
    #所属グループのサイズ確認
    #print(uni_f.size(3))