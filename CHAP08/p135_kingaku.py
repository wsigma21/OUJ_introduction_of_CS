# p135
# アルゴリズムの例
# 貪欲法を用いた支払い
pay = int(input("金額を入力してください："))
type = [500, 100, 50, 10, 5, 1]
for i in type:
    num = int(pay / i)
    if num >= 1:
        print(str(i) + "円玉を" + str(num) + "枚払います")
        pay -= i * num  # 支払い
