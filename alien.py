alien_0 = {'color': 'green', 'points': 5}   #字典，花括号标识，看起来像结构体
print(alien_0['color'])
print(alien_0['points'])

print(alien_0)
alien_0['x_position'] = 0       #字典添加元素
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'     #修改字典的值
print(alien_0['color'])

print(alien_0)
del alien_0['points']           #删除键
print(alien_0)