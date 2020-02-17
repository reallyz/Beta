import requests_html
from io import BytesIO
from PIL import Image
#bytes
#将bytes结果转化为字节流
sess=requests_html.HTMLSession()
url='https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2886697051,711988285&fm=15&gp=0.jpg'
bytes_=sess.get(url).content
# 这里就可以直接写入文件了
stream=BytesIO(bytes_)
# 这里stream.getvalue后可以直接以wb的方式写入文件
# 但是要修改文件大小所以有接下来的几步
img=Image.open(stream)
imgresize=img.resize((900,600))
imgByteArr=BytesIO()
imgresize.save(imgByteArr,format('PNG'))#写回字节流
imgByteArr=imgByteArr.getvalue()# 从字节流拿到bytes
with open(r'test2.png','wb') as f:
    f.write(imgByteArr)

