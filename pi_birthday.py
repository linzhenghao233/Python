from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.strip()

birthday = input("输入你的生日（年月日）：")
if birthday in pi_string:
    print('你的生日在π的前100万位小数中')
else:
    print('你的生日不在π的前100万位小数中')