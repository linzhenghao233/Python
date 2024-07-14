class Dog:                              #类的首字母大写(约定俗成)
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):      #类中的函数称为方法
        """初始化属性name和age"""        #调用此类时自动调用__init__()
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()