# p127
# アルゴリズムの例
# ユークリッドの互除法
a = int(input("aを入力してください："))
b = int(input("bを入力してください："))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print("最大公約数は" + str(a) + "です")
