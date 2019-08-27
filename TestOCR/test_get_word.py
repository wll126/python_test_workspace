# coding:utf-8

import tesserocr
from PIL import Image
img_path='images/word.png'
image=Image.open(img_path)
image=image.convert('L')
threshold=127
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
image=image.point(table,'1')
image.show()


result=tesserocr.image_to_text(image,'chi_sim')
result2=tesserocr.file_to_text(img_path,'chi_sim')
print(result)
print(result2)

