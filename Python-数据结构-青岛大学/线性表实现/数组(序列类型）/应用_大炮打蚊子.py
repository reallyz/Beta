import numpy as np
import re
import random
# 地图加载
n,m=input('pleae enter row and col\n').split()
n,m=eval(n),eval(m)
array1=np.zeros([n,m])
for i in range(n):
    s = input('按行输入地图:')
    print(f'第{i}行')
    index=re.finditer('W',s)
    for j in index:
        array1[i,j.start()]=2
print(array1)
# 随机发射n发炮弹
p=eval(input('number of bullet\n'))
for i in range(p):
    x=random.randint(0,n)
    y=random.randint(0,m)
    loc=array1[x,y]
    #一技致命
    


