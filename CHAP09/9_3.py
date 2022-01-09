# 入力された年月のカレンダーを表示するプログラム
N = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
y = int(input("年を入力してください："))
m = int(input("月を入力してください："))
d = 1
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0: # yが閏年なら
    N[1] += 1 #2月に1日追加
if m <= 2:
    y = y - 1
    m = m + 12
# ツェラーの公式で曜日を求める
w = (y + int(y/4) - int(y / 100) + int(y / 400) + int((13 * m + 8) / 5 + d)) % 7

#曜日行の表示
for i in range(7): 
    print(Day[i] + " ", end="")
print("") #改行

# 先頭行の空白を表示
for i in range(w):
    print("    ", end="")

# 13,14 月を1,2月に戻す
if m > 12:
    m = m - 12
# m = (m - 1) % 12 + 1で求められる

# 表示
for i in range(1, N[m-1]+1):
    if i < 10:
        print(" ", end="") # 1桁の場合は空白1つ追加
    print(" " + str(i) + " ", end="") #日の表示
    if (w + i) % 7 == 0:#土曜なら改行
        print("")
print("")