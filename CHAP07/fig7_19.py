# 剰余を使わないFizzBuzz
n3 = 3
n5 = 5
for i in range(1, 101):
    fizz = ""
    buzz = ""
    if i == n3:
        fizz = "Fizz"
        n3 += 3
    if i == n5:
        buzz = "Buzz"
        n5 += 5
    if fizz == buzz:
        print(i)
    else:
        print(fizz + buzz)
