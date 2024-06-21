bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1]) #-1访问列表最后一个元素，负号代表方向：从尾到头

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)