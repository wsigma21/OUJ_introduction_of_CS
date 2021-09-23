# 演習問題7.1
# 入力された最高気温によって表示を変更
temp = int(input("最高気温を入力してください："))
if temp >= 35:
    m = "猛暑日"
elif temp >= 30:
    m = "真夏日"
elif temp >= 25:
    m = "夏日"
else:
    m = "暑くないです"
print(m)
