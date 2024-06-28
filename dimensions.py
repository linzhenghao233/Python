dimensions = (200, 50)  #元组，不可改变的列表
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 1  修改时会报错

dimensions = 1,     #严格上元组由逗号标识
                    #元组可重新定义
#dimensions[0] = 2
print(dimensions[0])

foods = ("cake", "sugar", "beef", "pork", "wine")
for food in foods:
    print(food)
#foods[0] = "person"
#修改元组会报错
foods = ("cake", "sugar", "ice-cream", "water", "wine")
for food in foods:
    print(food)