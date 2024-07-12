#8.6
def city_country(city, country):
    message = f"{city}, {country}"
    return message

message = city_country('shanwei', 'China')
print(message)

#8.7
def make_album(singer, album, amount=None):
    if amount:
        message = {'singer': singer, 'album': album, 'amount': amount}
    else:
        message = {'singer': singer, 'album': album}
    
    return message

album = make_album('交工乐队', '《菊花夜行军》', 1)
print(album)
album = make_album('陶喆', '《黑色柳丁》')
print(album)
album = make_album('徐佳莹', '《寻人启事》')
print(album)

#8.8
while True:
    singer = input("请输入歌手名字：(输入'q'退出)")
    if singer == 'q':
        break
    album = input("输入TA的专辑名：(输入'q'退出)")
    if album == 'q':
        break
    message = make_album(singer, album)
    print(message)