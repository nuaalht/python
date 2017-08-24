# 使用try-except代码块处理可能引发的异常
# 如果try代码没问题,跳过except模块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can not divide by zero! ")
# 使用异常来避免崩溃
'''
print("Give me two numbers, and I'll divide them. ")
print("Enter 'q' to quit. ")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero! ")
    else:
        print(answer)
'''
# 处理FileNotFoundError
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
# 分析文本
title = "Alice in Wonderland"
print(title.split())

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
# 使用多个文件
import word_count
filename = 'alice.txt'
word_count.count_words(filename)
filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in filename:
    word_count.count_words(file)
# 程序发生错误时一声不吭 except用pass语句
