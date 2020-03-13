import requests
import os

# 百度关键词
# kv = {'wd': 'Python'}
# r = requests.get("http://www.baidu.com", params=kv)

# 网络图片存储
root = '/Users/piwenjing/PycharmProjects/untitled2/com/img/'
url = 'http://pic.962.net/up/2017-6/14986998648934568.jpg'
# 用原来的文件名作为文件名
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb')as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('五年级已经存在')
except:
    print('爬取失败')
