def make_pizza(size, *toppings):      #接受任意个实参，类似指针，接收后用元组存储
    """打印顾客点的pizza"""
    print(f"制作一个{size}寸的披萨，添加以下配料：")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):    #两个'*'会创建一个字典
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                             location='princeton', 
                             field='physics')
print(user_profile)