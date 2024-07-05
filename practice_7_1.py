#7.1
car = input("你想要什么车？")
print(f"我看看有没有{car}")

#7.2
num = input("你们多少个人用餐？")
if int(num) > 8:
    print("抱歉，没有空桌。")
else:
    print("有空桌")

#7.3
num = input("输入一个整数：")
if int(num) % 10 == 0:
    print(f"{num}是10的整数倍")
else:
    print(f"{num}不是10的整数倍")
