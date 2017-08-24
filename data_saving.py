'''使用json.dump()和json.load()'''
'''格式：JSON(JavaScript Object Notation)'''
import json
# 写
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
# 读
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)