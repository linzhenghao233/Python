players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0 : 3])
print(players[1 : 4])
print(players[: 4])
print(players[2 :])
print(players[-3 :])
#可写第三个参数表示步长
#确定的起始下标 : 比实际的结尾下标多1 : 步长

print("Here are the first three players on my team:")
for player in players[: 3]:
    print(player.title())

temp = players[:]   #参数都省略，复制整个列表
temp = players      #这种方式相当于赋值了指针