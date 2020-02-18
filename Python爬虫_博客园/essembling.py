import requests
import re
import os
from bs4 import BeautifulSoup

def get_html_text(url):
    try:
        r=requests.request(url=url,method='Get',timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
        # 这里返回的是字符串格式
    except:
        return '产生异常'
def savefile(path,file):
    with open(path,'a') as f:
        f.write(file)


if __name__ == '__main__':
    url='http://baijiahao.baidu.com/s?id=1598724756013298998&wfr=spider&for=pc'
    page=get_html_text(url)
    # 根据网页结构，用正则来匹配
    # 格式一定要设置好,不然很tricky
    pattern='<span class="bjh-p">(.*?)</span>'
    duanzi=re.findall(pattern,page)
    path=r'duanzi.txt'
    # 文件读写的问题,明天来解决
    for i in duanzi:
        savefile(path,i)