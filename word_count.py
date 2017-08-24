def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry the file, " + filename + " does not exist."
        # pass 发生错误时一声不吭
        print(msg)
    else:
        # 计算文件包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words")