import random  # 引入模块

secret = random.randint(1, 100)  # 随机生成0到100之间的整数
times = 3
while times:
    num = input("输入一个整数：")
    if num.isdigit():
        tmp = int(num)  # num赋值给tmp用于比较
        if tmp == secret:
            print("你猜对了")

        elif tmp < secret:
            print("小了")
            times = times - 1
        else:
            print("大了")
            times = times - 1
    else:
        print("输入的应该是数字！")
print("游戏结束")