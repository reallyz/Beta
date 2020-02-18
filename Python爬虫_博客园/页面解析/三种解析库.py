from bs4 import BeautifulSoup
from lxml.html import  etree # 解析后对象可以用xpath进行内容匹配
import parsel #解析后可以用xpath,re,css进行内容匹配
#解析器的种类：解析格式不一样
'''
BeautifulSoup(mk,'html.parser')
BeautifulSoup(mk,'lxml')
BeautifulSoup(mk,'xml')
BeautifulSoup(mk,'html5lib')
'''
# 对于解析后的对象怎么处理？