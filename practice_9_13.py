from random import randint, choice

#9.13
class Die:
    def __init__(self):
        self.sides = 6
        self.num = 1
    
    def roll_die(self):
        for i in range(self.num):
            print(randint(1, self.sides))

dice_6 = Die()
dice_6.num = 10
dice_6.roll_die()

dice_10 = Die()
dice_10.sides = 10
dice_10.num = 10
dice_10.roll_die()

dice_20 = Die()
dice_20.sides = 20
dice_20.num = 10
dice_20.roll_die()

#9.14
pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
lucky = []
for i in range(4):
    lucky.append(choice(pool))
print(lucky)

#9.15
my_ticket = [2, 5, 6, 8]
count = 0
while 1:
    count += 1
    for i in range(4):
        lucky.append(choice(pool))
    print(lucky)
    if(set(my_ticket) == set(lucky)):
        print(f"在第{count}次出奖中中奖")
        break
    lucky.clear()
