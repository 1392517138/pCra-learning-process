import requests
import bs4
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html,"lxml")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            #也可以tds = tr.find_all("td")
            tds = tr('td')
            #.string是取标签的字符串
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    #{3}表示用format第3个值进行填充，chr(12288)指中文空格
    #否则默认为西文字符
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    # {}是槽，\t是制表符 ^表示居中 数字表示，
    # print("{:^6}\t{:^12}\t{:^6}".format("排名","学校名称","总分"))

    #优化对齐后
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        # print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
        print(tplt.format(u[0], u[1], u[2],chr(12288)))
        # print("{:^10}\t{:^10}".format(u[0], u[2]))
if __name__ == '__main__':
    ulist = []
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    html = getHTMLText(url)
    fillUnivList(ulist,html)
    printUnivList(ulist,20)