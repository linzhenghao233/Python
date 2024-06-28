squares = [value ** 2 for value in range(1, 11)]    #列表推导式
print(squares)

#循环打印1-20
for value in range(1, 21):
    print(value)

#创建一个包含1-100万的列表并输出
arr = list(range(1, 1000001))
'''
for value in arr:
    print(value)
'''

#对arr列表使用min()、max()、sum()
print(f"最小值为：{min(arr)}")
print(f"最大值为：{max(arr)}")
print(f"和为：{sum(arr)}")

#创建1-20的奇数列表并打印
arr = list(range(1, 21, 2))
for value in arr:
    print(value)

#3的倍数
arr = list(range(3, 31, 3))
for value in arr:
    print(value)

#1-10的立方
arr = [value ** 3 for value in range(1, 11)]
for value in arr:
    print(value)