import requests
from bs4 import BeautifulSoup

url = 'https://baike.baidu.com/item/IP138%E6%9F%A5%E8%AF%A2/15731154?fr=aladdin'
# kv = {'user-agent':'Mozilla/5.0'}
r = requests.get(url)
r.encoding = r.apparent_encoding
print(r.status_code)
# print(r.text)
soup = BeautifulSoup(r.text, "lxml")
print(soup.a.previous_sibling)
