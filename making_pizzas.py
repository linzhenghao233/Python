import pizza_8_5                    #如原函数有输出函数，导入时会一起输出
from pizza_8_5 import make_pizza    #导入特定函数，用','隔开可同时导入多个函数
from pizza_8_5 import make_pizza as mp  #取别名
import pizza_8_5 as p
from pizza_8_5 import *             #导入模块的所有函数

pizza_8_5.make_pizza(16, 'pepperoni')
pizza_8_5.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')