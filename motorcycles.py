motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')     #追加元素：append()
print(motorcycles)
motorcycles.insert(0, 'test')   #在指定下标插入元素：insert()
print(motorcycles)
del motorcycles[0]              #删除指定下标元素：del
print(motorcycles)

popped_motorcycle = motorcycles.pop()   #弹出指定下标的值，空则弹出最后一个：pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('ducati')    #删除匹配的值：remove()
print(motorcycles)              #remove()只删除第一个匹配的值

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(f"{too_expensive.title()} is too expensive for me.")