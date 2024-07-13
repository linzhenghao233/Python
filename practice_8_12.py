#8.12
def make_sandwich(*foods):
    print("需要添加以下食材：")
    for food in foods:
        print(f"-{food}")

make_sandwich('鸡柳')
make_sandwich('鸡柳', '薄脆')
make_sandwich('热狗', '花生', '鸡柳')

#8.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

message = build_profile('政浩', '林', 兴趣='读书、摸鱼', 
                        最喜欢的语言='C语言', 
                        现在听的歌='苏运莹《等风停》')
print(message)

#8.14
def make_car(制造商, 型号, **其它):
    其它['name'] = 制造商
    其它['model'] = 型号
    return 其它

car = make_car('subaru', 'outback', color='blue', tow_pacjage=True)
print(car)