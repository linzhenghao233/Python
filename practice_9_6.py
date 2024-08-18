#9.6
from practice_9_4 import Restaurant, User

class IceCreamStand(Restaurant):
    def __init__(restaurant, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        restaurant.flavors = []
    
    def display(restaurant):
        for flavor in restaurant.flavors:
            print(flavor)


iceCream = IceCreamStand("五羊", "icecream")
iceCream.flavors = ["香芋", "香草", "榴莲"]
iceCream.display()


#9.8
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


#9.7
class Admin(User):
    def __init__(user, first_name, last_name):
        super().__init__(first_name, last_name)
        user.privileges = Privileges()
    
    def show_privileges(user):
        user.privileges.show_privileges()


Admin = Admin('zhenghao', 'lin')
Admin.show_privileges()


#9.9：见electric_car.py