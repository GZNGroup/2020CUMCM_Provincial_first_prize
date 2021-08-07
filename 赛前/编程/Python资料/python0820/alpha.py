# 定义函数
def f(x):
    z = (x - 1.234) ** 3
    return z


# 定义初值
a, b = 0, 2

# 循环开始
for i in range(100):
    c = 0.5 * (a + b)
    if f(a) * f(c) >= 0:
        a = c
    else:
        b = c
    if abs(a - b) < 10 ** -6:
        print(i)
        break

# 控制台显示计算结果
print(a, b)

# 建立空列表（list）
d = []

# 循环开始
for i in range(100):
    if (i % 7 == 0) or ('7' in str(i)):
        d.append(i)

# 控制台输出数据
print(d)

