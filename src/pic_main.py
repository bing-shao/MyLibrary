# -*- coding:utf-8 -*-
import re
import requests


def downloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 1
    print('关键词：' + keyword + '的图片，开始下载...')
    for each in pic_url:
        print('正在下载' + str(i) + '张图片，地址：' + str(each))
        try:
            pic = requests.get(each, timeout = 10)
        except requests.exceptions.ConnectionError:
            print('错误，当前图片无法下载')
            continue

        dir = 'D:/picture/' + keyword + '_' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

if __name__ == '__main__':
    word = input("Input key word:")
    url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%A2%A6%E5%B9%BB%E8%A5%BF%E6%B8%B8"
    result = requests.get(url)
    downloadPic(result.text, word)
