import requests_html
from io import BytesIO
from PIL import Image

sess=requests_html.HTMLSession()
url='https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2886697051,711988285&fm=15&gp=0.jpg'
bytes_=sess.get(url).content
stream=BytesIO(bytes_)
img=Image.open(stream)
imgresize=img.resize((900,600))
imgresize.save('\mypythonpillow.jpg','JPEG')

