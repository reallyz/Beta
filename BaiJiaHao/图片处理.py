from PIL import Image

def Image_Resize(path):
    im=Image.open(path)
    imresize=im.resize((900,600))
    imresize.save('tess.jpg','JPEG')

if __name__=="__main__":
    path=r"C:\Users\HP\Pictures\Camera Roll\006MEyHsly1g9hatidopyj30zk0okgtj.jpg"
    Image_Resize(path)