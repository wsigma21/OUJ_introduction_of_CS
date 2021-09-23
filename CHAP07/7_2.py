# 演習問題7.2
# 1~100までの指定された数の倍数と、それらの和を表示
num = int(input("1~100の間の数字を入力してください："))
if num < 1 or 100 < num:
    print("数字は1~100の間で入力してください")
else:
    sum = 0
    for i in range(num, 101):
        if i % num == 0:
            print(i)
            sum += i
    print("和：" + str(sum))
