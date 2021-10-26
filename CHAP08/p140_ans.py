# p140
# アルゴリズムの例
# 貪欲法を用いた支払い
# 所持金に限度がある場合
pay = int(input("金額を入力してください："))
type = [[500, 1], [100, 2], [50, 3], [10, 12], [5, 4], [1, 10]]
for i, j in type:
    num = int(pay / i)
    if num >= 1:
        if num > j:
            num = j  # 所持金の中で支払える枚数
            print(str(i) + "円玉を" + str(num) + "枚払います")
            pay -= i * num  # 支払い
if pay > 0:
    print("支払いきれませんでした。")
