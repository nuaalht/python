with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip()) # 去除行
# 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt'
with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))

# 圆周率中包含你的生日吗
filename = 'pi_million_digits.txt'
with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your bithday does not appear in the first million digits of pi!')