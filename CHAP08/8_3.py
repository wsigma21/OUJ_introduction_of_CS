# 図8.5のプログラム（p130.py)を利用して、分母・分子を入力してもらい、その分数を約分して表示するプログラムを作成せよ。
mom = int(input("分母を入力してください："))
child = int(input("分子を入力してください："))

# 分母分子の最大公約数を求める
a = mom
b = child
if a < b:
    tmp = b
    b = a
    a = tmp
while b != 0:
    tmp = b
    b = a % b
    a = tmp

if a == 1:
    # 互いに素である場合
    print("約分できませんでした")
else:
    # 最大公約数で約分する
    print(str(int(mom / a)) + "分の" + str(int(child / a)))
