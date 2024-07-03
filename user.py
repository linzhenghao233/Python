user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():   #items()成对返回
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in user_0.keys():       #keys()会返回所有的键
    print(f"Key:{key}")

for value in user_0.values():
    print(f"Value:{value}")

#set()可去除字典中重复的值，成为集合，可用花括号为标识创建