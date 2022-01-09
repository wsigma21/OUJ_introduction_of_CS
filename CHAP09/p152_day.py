# 入力された年月日の曜日を求めるプログラム
Day = ["日", "月", "火", "水", "木", "金", "土"]
y = int(input("年を入力してください："))
m = int(input("月を入力してください："))
d = int(input("日を入力してください："))
if m <= 2:
    y = y - 1
    m = m + 12
# ツェラーの公式
zeller_congruence = (y + int(y/4) - int(y / 100) + int(y / 400) + int((13 * m + 8) / 5 + d)) % 7
w = zeller_congruence
print(str(Day[w]) + "曜日です")
