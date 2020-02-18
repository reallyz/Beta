

# url(统一资源定位符）的编码方式
# 就是将中文字符串进行utf8编码
# 然后得到编码后的对象转换字符串
# 去掉开头的b'以及末尾的',
# 然后再将\x转换成%,
# 再将里面内容x变成e
# 最后将字符串小写变成大写

a='中'
a1=str(a.encode('utf8')).strip("b'").replace('\\x','%').replace('x','e').upper()
print('自己的编码：',a1)
# 使用urllib库里面的函数进行编码和解码
from urllib import parse
a2=parse.quote(a)
print(a2)
print('解码')
print(parse.unquote(a1))
print(parse.unquote(a2))