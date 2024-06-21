cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()                     #按首字母从小到大排序sort()
print(cars)                     #会改变列表原有的排序
cars.sort(reverse = True)       #方向排序sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))             #不改变列表原有的排序：sorted(列表名)
print(cars)
print(sorted(cars, reverse = True))

cars.reverse()                  #方向打印：reverse()
print(cars)                     #会改变原列表

len = len(cars)
print(len)