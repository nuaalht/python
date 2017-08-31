from selenium import webdriver
import time

import urllib.request

from bs4 import BeautifulSoup

import html.parser

def main():
    #****** Open chrome  driver and type the website that you want to view ****

    driver = webdriver.Chrome('C:\\Users\\HuiTao Lv\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe') # 打开浏览器

    # 列出来你想要下载图片的网站
    # driver.get("https://www.zhihu.com/question/35931586") # 你的日常搭配是什么样子？
    # driver.get("https://www.zhihu.com/question/61235373") # 女生腿好看胸平是一种什么体验？
    # driver.get("https://www.zhihu.com/question/28481779") # 腿长是一种什么体验？
    # driver.get("https://www.zhihu.com/question/19671417") # 拍照时怎样摆姿势好看？
    # driver.get("https://www.zhihu.com/question/20196263") # 女性胸部过大会有哪些困扰与不便？
    # driver.get("https://www.zhihu.com/question/46458423") # 短发女孩要怎么拍照才性感？
    driver.get("https://www.zhihu.com/question/26037846") # 身材好是一种怎样的体验？

# ********Scroll to the bottom, and click the "view more" button ****
    def execute_times(times):

        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 滑动到浏览器底部
            time.sleep(2) # 等待页面加载
            try:
                driver.find_element_by_css_selector("button.QuestionMainAction").click() # 选中并点击页面底部的加载更多
                print("page" + str(i)) # 输出页面页数
                time.sleep(1) # 等待页面加载
            except:
                break

    execute_times(3) # 加载五个页面
# ****** Prettify the html file and store raw data file

    result_raw = driver.page_source # 原网页HTML信息
    result_soup = BeautifulSoup(result_raw, 'html.parser')

    result_bf = result_soup.prettify() # 结构化原HTML文件
    # with open("./output/rawfile/raw_result.txt", 'w') as girls: # 存储路径里的文件夹要事先创建
    #     girls.write(result_bf)
    # girls.close()
    print("Store raw data successfully!!!")
# ******* Find all <nonscript> nodes and store them *********
    with open("./output/rawfile/noscript_meta.txt", 'w') as noscript_meta: # 存储路径里的文件夹需要事先创建
        noscript_nodes = result_soup.find_all('noscript') # 找到所有<noscript>node
        noscript_inner_all = ""
        for noscript in noscript_nodes:
            noscript_inner = noscript.get_text() # 获取<noscript>node 内部内容
            noscript_inner_all += noscript_inner + "\n"

        noscript_all = html.parser.unescape(noscript_inner_all) # 将内容转码并存储
        #noscript_meta.write(noscript_all)

    noscript_meta.close()
    print("Store noscript meta data successfully!!!")

# ********** Store meta data of imgs ******************
    img_soup = BeautifulSoup(noscript_all, 'html.parser')
    img_nodes = img_soup.find_all('img')
    with open("./output/rawfile/img_meta.txt", 'w') as img_meta:
        count = 0
        for img in img_nodes:
            if img.get('src') is not None:
                img_url = img.get('src')

                line = str(count) + "\t" + img_url  + "\n"
                img_meta.write(line)
                urllib.request.urlretrieve(img_url, "./output/image/" + str(count) + ".jpg") # 一个一个下载图片
                count += 1

    img_meta.close()
    print("Store meta data and images successfully!!!")

if __name__ == '__main__':
    main()