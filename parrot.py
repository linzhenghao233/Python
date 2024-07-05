message = input("Tell me something, and I will repeat it back to you:")
#用户输入后回车输入
print(message)

#提示过长时
prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")

#input()是字符串
#int()强制转换成整数
#字符串和整数不能比较