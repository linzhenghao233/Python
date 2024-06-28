cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':    #区分大小写
        print(car.upper())
    else:
        print(car.title())

print('audi' in cars)   #检测某个元素是否在列表中，返回True或False
print('audi' not in cars)   #检测某个元素是否不在列表中