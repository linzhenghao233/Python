#9.4
class Restaurant:
    def __init__(restaurant, restaurant_name, cuisine_type):
        restaurant.restaurant_name = restaurant_name
        restaurant.cuisine_type = cuisine_type
        restaurant.number_served = 0

    def describe_restaurant(restaurant):
        print(f"{restaurant.restaurant_name}")
        print(f"{restaurant.cuisine_type}")

    def open_restaurant(restaurant):
        print(f"{restaurant.restaurant_name}正在营业。")

    def set_number_served(restaurant, number):
        restaurant.number_served = number
        print(f"有{restaurant.number_served}人就餐。")
    
    def increment_number_served(restaurant, number):
        restaurant.number_served += number
        print(f"加{restaurant.number_served}个位。")

restaurant = Restaurant('林记炒饭', '三丝炒面')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.increment_number_served(100)
restaurant.set_number_served(6)

#9.5
class User:
    def __init__(user, first_name, last_name):
        user.first_name = first_name
        user.last_name = last_name
        user.login_attempts = 0

    def describe_user(user):
        print(f"{user.first_name}")
        print(f"{user.last_name}")

    def greet_user(user):
        print(f"{user.first_name} {user.last_name}, Hello!")

    def increment_login_attempts(user):
        user.login_attempts += 1

    def reset_login_attempts(user):
        user.login_attempts = 0

user01 = User('Zhenghao', 'Lin')
user01.greet_user()
user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()
print(user01.login_attempts)
user01.reset_login_attempts()
print(user01.login_attempts)