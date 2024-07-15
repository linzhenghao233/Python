#9.1
class Restaurant:
    def __init__(restaurant, restaurant_name, cuisine_type):
        restaurant.restaurant_name = restaurant_name
        restaurant.cuisine_type = cuisine_type

    def describe_restaurant(restaurant):
        print(f"{restaurant.restaurant_name}")
        print(f"{restaurant.cuisine_type}")

    def open_restaurant(restaurant):
        print(f"{restaurant.restaurant_name}正在营业。")

restaurant = Restaurant('林记炒饭', '三丝炒面')
restaurant.describe_restaurant()
restaurant.open_restaurant()


#9.2
restaurant01 = Restaurant('隆江猪脚饭', '猪脚饭')
restaurant01.describe_restaurant()

restaurant02 = Restaurant('沙县大酒店', '蒸饺')
restaurant02.describe_restaurant()

restaurant03 = Restaurant('Test', 'test')
restaurant03.describe_restaurant()


#9.3
class User:
    def __init__(user, first_name, last_name):
        user.first_name = first_name
        user.last_name = last_name

    def describe_user(user):
        print(f"{user.first_name}")
        print(f"{user.last_name}")

    def greet_user(user):
        print(f"{user.first_name} {user.last_name}, Hello!")

user01 = User('Zhenghao', 'Lin')
user01.greet_user()