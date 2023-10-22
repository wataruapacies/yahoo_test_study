class UnionFind:
    def __init__(self, N):
        # _leader[x]：頂点xが属するグループのリーダー
        #             頂点xがリーダーであるときは-1
        # _size[x]：頂点xがリーダーであるときは属するグループの要素数
        #           頂点xがリーダーでないときは-1
        self._leader = [-1 for _ in range(N)]
        self._size = [1 for _ in range(N)]
    
    def find(self, x):
        if self._leader[x] == -1: return x
        
        vertices = []
        while self._leader[x] != -1:
            vertices.append(x)
            x = self._leader[x]
        
        # 経路圧縮
        for y in vertices:
            self._leader[y] = x
        
        return x
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return False

        # union-by-size
        if self._size[x] < self._size[y]: x, y = y, x

        self._leader[y] = x
        self._size[x] += self._size[y]
        self._size[y] = -1

        return True
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return self._size[self.find(x)]
    
    def is_leader(self, x):
        return self._leader[x] == -1


H, W = map(int, input().split())
S = [input() for _ in range(H)]

uf = UnionFind(H * W)

dir = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '.': continue

        for k in range(8):
            ni, nj = i + dir[k][0], j + dir[k][1]
            if not(0 <= ni < H and 0 <= nj < W): continue

            if S[ni][nj] == '#': uf.union(i * W + j, ni * W + nj)

ans = 0
for i in range(H):
    for j in range(W):
        # print(f'{i = } {j = } {S[i][j] = } {uf.is_leader(i * W + j)= }')
        if S[i][j] == '#' and uf.is_leader(i * W + j): ans += 1

print(ans)
# print(uf._leader)