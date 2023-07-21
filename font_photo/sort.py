import os
from PIL import Image
import numpy as np
path="."
im_dict={}
for i in os.listdir(path):
	if '.png' in i:
		img=Image.open(i)
		data=np.asarray(img, dtype="int32")
		k=data.sum()
		im_dict[i]=k
	else:
		continue

sorted_pix=sorted(im_dict.items(), key=lambda x:x[1])
sl=[i[0] for i in sorted_pix]
for i in os.listdir(path):
	if '.png' in i:
		os.rename(i, str(sl.index(i))+'.png')


