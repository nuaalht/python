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
# 弹出列表中人已死指定的元素
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