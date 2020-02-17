import requests

'''
这里仅限于页面获取
'''

# 背景知识：http协议中的六个方法
'''
Get:请求获取url位置的资源
Head:请求获取url位置的资源的响应报告，和头部信息
Post:请求获取url位置的资源后附加用户新的数据
Put:请求获取url位置储存一个资源，覆盖原url位置资源
Patch:请求局部更新url位置资源，及改变该处资源的部分内容
Delete:请求删除url位置储存的资源
'''
# requests的方法与协议方法一一对应，
requests.request()# 可设置请求格式

# 获取返回对象的属性
'''
r.status_code:状态码
r.text:响应内容转成字符串格式
r.content:响应内容转成二进制格式
r.encoding:编码方式
r.apparent_encoding:更精确的编码方式
r.json：响应内容以json格式保存
r.headers:响应的请求头
r.cookies:响应体的cookie
r.history:重定向的历史
'''
# 异常
'''
注意，除了这样异常，还专门有一个：当r.status_code
不是200(正常响应）时， r.raise_for_status()抛出异常
'''
# http协议不仅能下载数据，还能上传数据
# 所有requests库里有参数来指定上传数据的格式
'''
用于协议的参数：
                headers:字典类型，模拟浏览器
                cookies:字典类型：cookie信息
                auth:元组，认证功能
                timeout:超时时间
                proxies:字典，设定代理服务器
                allow_redirects:bool,重定向
                cert:本地SSL证书路径
                verify:bool,是否认证
                stream:bool，获取内容立即下载
用于上传的数据格式：
                data：字典，字节流，文件对象，
                json:JSON格式的数据
                file:file={'文件名'，open(文件路径)，'rb'}
用于对url进行修改：
                params：字典               
'''
# 一般爬取框架try...except(不中断执行
def get_html_text(url):
    try:
        r=requests.request(url=url,method='Get',timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == '__main__':
    get_html_text('http://www.baidu.com')
