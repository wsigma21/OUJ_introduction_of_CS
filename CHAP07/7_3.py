# 演習問題7.3
# 入力された変数n,rを元にnのr乗を出力
# rは0以上、負の数が入力された場合は警告

n = int(input("nを入力："))
r = int(input("rを入力："))
if r < 0:
    print("rには0以上の数を入力してください")
else:
    result = 1
    # for i in range(1, r+1):
    # ans
    for i in range(r):  # r回の繰り返し
        result = result * n
    print(str(n) + "の" + str(r) + "乗は" + str(result))
