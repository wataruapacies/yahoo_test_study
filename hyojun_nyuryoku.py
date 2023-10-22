n , m = map(int,input().split())
#数字２つ

a = list(map(int,input().split()))
#横並び数字リスト

s = [list(input()) for i in range(n)]
#縦並び文字列リスト

s = [input() for i in range(n)]
#縦並び文字列リスト

in_str = input().split()
#横連続文字列をリストとして入力

n , m = map(int,input().split())

a = []
b = []

for _ in range(m):
    ai , bi = map(int,input().split())
    a.append(ai)
    b.append(bi)

#2組の改行ごとにリスト追加