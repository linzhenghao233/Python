def greet_user():
    '''显示简单的问候语'''
    print("Hello!")

greet_user()

def greet_user(username):
    '''显示简单的问候语'''
    print(f"Hello!{username.title()}.")

greet_user('linzhenghao')

#位置实参
def describe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'miumiu')
describe_pet('dog', 'none')
#关键字实参
describe_pet(pet_name='shit', animal_type='dog')

#默认值
def describe_pet(pet_name, animal_type = 'cat'):
    '''显示宠物信息'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('miumiu')