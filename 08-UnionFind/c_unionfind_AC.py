# https://atcoder.jp/contests/abc231/tasks/abc231_d


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
    
    
# 初期化：変数名=UnionFind(要素の数)
UF=UnionFind(10)

# グループ化：変数名.merge(要素番号1,要素番号2)
UF.merge(0,2)
UF.merge(1,3)
UF.merge(3,0)

# グループリーダー(根)の確認：変数名.leader(要素番号)
leader_x=UF.leader(1)

# 同一グループかの確認：変数名.same(要素番号1,要素番号2)
if UF.same(1,5)==True:
    print("同一グループ")
else:
    print("別グループ")

# 所属するグループのサイズ確認：変数名.size(要素番号)
size_x=UF.size(1)

# グループ全体の確認：変数名.groups()
print(UF.groups())