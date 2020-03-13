#  01
# import requests
# import json
#
# def get_translate_date(word=None):
#     url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#
#     From_data = {
#         'i': word,
#         'from': 'AUTO',
#         'to': 'AUTO',
#         'smartresult': 'dict',
#         'client': 'fanyideskweb',
#         'salt': '15839928661186',
#         'sign': 'e22bddbd9eb882fc6679af5832a06a1c',
#         'ts': '1583992866118',
#         'bv': '983a2bbd012bf3b78f96f4764a0fa9fe',
#         'doctype': 'json',
#         'version': '2.1',
#         'keyfrom': 'fanyi.web',
#         'action': 'FY_BY_REALTlME'
#     }
#     response = requests.post(url,From_data)
#     content = json.loads(response.text)
#     print(content)
# if __name__ == '__main__':
#     get_translate_date('我爱中国')

# 02

import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':

    url = 'http://news.sina.com.cn/hotnews/'
    strhtml = requests.get(url)
    
    soup = BeautifulSoup(strhtml.text, 'lxml')
    data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
    for item in data:
        result = {
            'title': item.get_text(),
            'link': item.get('href'),
            'ID': re.findall('\d+', item.get('href'))
        }
        print(result)
