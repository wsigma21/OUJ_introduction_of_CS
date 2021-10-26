# p130
# アルゴリズムの例
# ユークリッドの互除法(割り算を使用)
a = int(input("aを入力してください："))
b = int(input("bを入力してください："))
# a < bだったら、aとbを入れ替える
if a < b:
    tmp = b
    b = a
    a = tmp
while b != 0:
    tmp = b
    b = a % b
    a = tmp

print("最大公約数は" + str(a) + "です")
