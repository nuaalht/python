message = "From lht"
print("hello "+"python "+ message.title() + " !")
print(2**2)
age = 23
# 祝某人生日快乐
message = "Happy " + str(age) + "rd Birthday !"
print(message)
# list
bicycles = ['trek','cannodale','redline','specialized']
print(bicycles[0])
print(bicycles[0].title())
# 在列表末尾增加数据
bicycles.append('honda')
print(bicycles)
# 插入数据
bicycles.insert(0,'suzuki')
print(bicycles)
# 删除列表中元素
del bicycles[0]
print(bicycles)
# 从列表中删除，并接着只用这个数据
popped_bicycles = bicycles.pop()
print(bicycles)
print(popped_bicycles)
# 弹出列表中指定的元素
first_owned = bicycles.pop()
print('My first owned bicycle is' + first_owned + "!")
# 根据值删除某个元素
bicycles.remove('cannodale')
print(bicycles)
# 组织列表
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
print(sorted(cars))
# 逆序排列
cars.sort(reverse=True)
print(cars)
print(len(cars))
# 遍历整个列表
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
print(magician)
for magician in magicians:
    print(magician.title() + ",that was a great trick!\n")
# 创建数值列表
for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)
# 指定步长
even = list(range(2,11,2))
print(even)
squares =[]
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
digits = list(range(0,10))
print(min(digits))
print(max(digits))
print(sum(digits))
# 列表的解析
squares = [value**2 for value in range(1,11)]
print(squares)
# 列表的切片
players = ['a','b','c','d','v']
print(players[1:3])
print(players[:3])
# 打印最后三名人员
print(players[-3:])
# 复制整个列表，单纯的复制指向同一个数据存存储空间
my_players = players[:]
print(my_players)
# 元组，不可变的列表称之为元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
# 修改元组变量
dimensions = (400,500)
print(dimensions)
# if条件语句
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# 检查不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
# 检查多个条件
# and or
#检查是否在列表中
requested_topping = ['mushrooms','onions','pineapple']
print('mushroom' in requested_topping)
# 检查是否不包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
# 布尔表达式： True, False
# 看到70页
# if - elif - else语句,可省略else
age = 12
if age < 4:
    print('Your admission cost is $0')
elif age < 18:
    print('Your admission cost is $5')
else:
    print('Your admission cost is $10')
# 检查特殊元素
resquested_toppings = ['mushroom','green peppers','extra cheese']
if resquested_toppings:
    for resquested_topping in resquested_toppings:
        print('Adding ' + resquested_topping + '.')
    print('\nFinished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')
# 字典,字典是一系列 键——值 对
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print('Your just earned ' + str(new_points) + ' points')
# 添加键——值 对
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
# 创建一个空字典往里面添加数值
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# 修改字典中的值
alien_0['color'] = 'yellow'
# interseting example
alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
print("Original x_positon： " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x_position: ' + str(alien_0['x_position']))
# 删除键——值 对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
# 遍历字典
user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi'
          }
for Key, Value in user_0.items():
    print("\nKey: " + Key)
    print("\nValue: " + Value)
# 遍历键
for key in user_0.keys():
    print(key.title())
# 按顺序遍历字典中所有的键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil1': 'python',
    }
for name in (sorted(favorite_languages.keys())):
    print(name.title() + ", thank you for taking the poll.")
# 遍历字典中所有的值
for language in favorite_languages.values():
    print(language.title())
# 使用set来创建列表
for language in set(favorite_languages.values()):
    print(language.title())
print(language)
# 嵌套 字典存储在列表中，列表作为值存储在字典中
# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外心人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print('Total numbers of aliens: ' + str(len(aliens)))
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
# 在字典中存储列表
# 存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }
# 概述所点的披萨的信息
for topping in pizza['toppings']:
    print('\t' + topping)
# 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# 用户输入和While循环,选中后,ctrl + / 注释多行
# message = input('Tell me something, and I will repeat it back to you: ')
# print(message)
# name = input('Please enter your name: ')
# print('Hello, ' + name + '!')

# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)

# 使用int()来获取数值输入
'''
height = input('How tall are you, in inches? ')
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
'''
'''
# 求模运算符,将数相除并返回余数
number = input("Enter a number, and I'll tell you if it even or odd: ")
number = int(number)
if number%2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")
'''
# while循环
'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 让用户何时选择退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
'''
# 看到106页
# 让用户选择退出
# prompt = "If you want to quit,enter quit"
# prompt += "else, We will return what you enter: "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# 使用标志
'''
prompt = "If you want to quit,enter quit"
prompt += "else, We will return what you enter: "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
'''
# 使用break退出循环
'''
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
'''
# 在循环中使用continue,Python忽略余下的代码,并返回循环的开头
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# 避免无限循环
# 使用while循环来处理列表和字典
# 在列表之间移动元素
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
# 使用用户输入来填充字典
'''
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n---Poll Results---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
'''
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("What is your name? ")
#     food = input("What is your favourite food? ")
#     responses[name] = food
#     polling_active = input("Do you want to add someone else? (yes/no) ")
#     if polling_active == 'no':
#         polling_active = False
# print("--- the dict ---")
# print(responses)

# 函数
def greet_user():
    '''显示简单的问候语'''
    print("hello")
# 调用
greet_user()
# 向函数传递信息
def greet_user(username):
    '''显示简单的问候语'''
    print("hello " + username.title() + " !")
greet_user('jesse')
# 实参和形参,传递实参(位置实参)
def descibe_pet(animal_type, pet_name):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
descibe_pet('hamster', 'harry')
# 关键字实参
descibe_pet(animal_type='hamster', pet_name='harry')
descibe_pet(pet_name='harry', animal_type='hamster')
# 默认值,给形参默认值
def descibe_pet(pet_name, animal_type='dog'):
    '''显示宠物信息'''
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
descibe_pet(pet_name='willie')
descibe_pet('willie')
descibe_pet(pet_name='harry', animal_type='hamster')
# 等效的函数调用
# 返回值
def get_formatted_name(first_name, last_name):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    '''返回整洁的姓名'''
    full_name = first_name + ' ' +  middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
# 返回字典
def build_person(first_name, last_name):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
def build_person(first_name, last_name, age=''):
    '''返回一个字典，其中包含有关一个人的信息'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','lee',18)
print(musician)
# 结合使用函数和while循环
'''
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name：")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
'''
# 传递列标
def greet_users(names):
    """向列表中每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    '''
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    :param unprinted_designs:
    :param completed_models:
    :return:
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 根据模拟设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    '''显示所有打印好的模型'''
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# 禁止函数修改列表
# 切片表示法 function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)
# 传递任意数量的实参
# 函数只有一个形参*toppings,创建一个toppings的空元组

def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print('- ' + topping)
    print(toppings)
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    '''概述要制作的披萨'''
    print("\nMaking a " + str(size) + "-inch pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    '''创建一个字典，其中包含我们知道的有关用户的一切'''
    # **user_info表示创建一个名为user_info的空字典
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
