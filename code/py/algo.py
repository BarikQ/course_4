import numpy as np
import random
import math
from PIL import Image
 
arr = np.asarray(Image.open('image_1.jpg'))
arrGS = np.asarray(Image.open('image_1.jpg').convert('LA'))
arr2 = arr.copy()

i = 0
j = 0
total = []
totalX = []
totalY = []

for rows in arrGS:
  for cols in rows:
    if (cols[0] > 10 or cols[1] < 255):
      total.append(cols)
      totalX.append(j)
      totalY.append(i)
    j += 1
  i += 1
  j = 0

centerX = math.ceil(sum(totalX) / len(totalX))
centerY = math.ceil(sum(totalY) / len(totalY))
print(centerX, centerY, arrGS[centerY][centerX])

arrGSCopy = arrGS.copy()
arrGSCopy[centerY][centerX] = [255, 255]
img2 = Image.fromarray(arrGSCopy)
img2.save('aimage_gs.png')

# RGB ========================

i = 0
j = 0
total = []
totalX = []
totalY = []

for rows in arr:
  for cols in rows:
    if (any(cols)): 
      for rgb in cols:
        if (rgb > 10):
          totalX.append(j)
          totalY.append(i)
    j += 1
  i += 1
  j = 0

centerX = math.ceil(sum(totalX) / len(totalX))
centerY = math.ceil(sum(totalY) / len(totalY))

print(centerX, centerY, arr[centerY][centerX])
arr2[centerY][centerX] = [255, 0, 0]
img2 = Image.fromarray(arr2, 'RGB')
img2.save('aimage_1.jpg')