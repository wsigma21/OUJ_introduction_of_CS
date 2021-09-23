# 演習問題7.4
# インド式九九の表
for i in range(1, 20):
    for j in range(1, 20):
        result = i * j
        if result <= 9:
            print("  ", end="")
        elif result <= 99:
            print(" ", end="")
        print(str(result)+" ", end="")
    print("")
