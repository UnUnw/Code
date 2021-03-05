'''六间房视频爬取'''
# 导入第三方库
import requests
import time
import os
from fake_useragent import UserAgent

# 随机请求头
ua = UserAgent()


# 定义一个六间房的类
class LiuJianFang():
    # 初始化对象
    def __init__(self):
        self.start_url = "https://v.6.cn/minivideo/getlist.php?act=recommend&page={}&pagesize=25"
        self.headers = {"User-Agent": ua.random}

    # 定义得到json文本的方法
    def get_json(self, url):
        time.sleep(1)
        json_text = requests.get(url, headers=self.headers).json()
        return json_text

    # 定义解析json文本和保存爬取视频的方法
    def paser_save_json(self, json_text):
        content = json_text["content"]["list"]
        if not os.path.exists("六间房"):  # 创建文件夹
            os.mkdir("六间房")
        for content in content:
            title = content["title"].replace("*", '')  # 替换标题中的敏感文字，windows文件中的敏感文字为？* ：" < > \ / |
            playurl = content["playurl"]  # 提取视频的地址
            r = requests.get(url=playurl, headers=self.headers)
            with open("六间房" + '/' + title + ".mp4", "wb") as f:
                print("正在下载：" + title)
                f.write(r.content)

    # 定义运行函数，实现主要逻辑
    def run(self):
        for i in range(10):
            url = self.start_url.format(i)
            json_text = self.get_json(url)
            self.paser_save_json(json_text)


# 程序运行接口
if __name__ == '__main__':
    video_spider = LiuJianFang()
    video_spider.run()
