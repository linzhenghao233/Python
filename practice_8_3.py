def make_shirt(size, shape='I Love Python'):
    print(f"你想要{shape}图案的{size}码的衣服。")

make_shirt('XXL', 'cat')
make_shirt(shape='cat', size='XXL')
make_shirt('XXXXL')
make_shirt('XXL')
make_shirt('XXXL', 'I Love C')

def describe_city(city, nation='中国'):
    print(f"{city}在{nation}。")

describe_city('广东')
describe_city('北京')
describe_city('纽约')   #题目要求写一个不在默认区域的