import cv2
import numpy as np
from random import randint

# Read, make grayscale ============================================
jpg = "bear.jpg"
img = cv2.imread(jpg)
r,g,b = img[:,:,0], img[:,:,1], img[:,:,2]
grayscale = r*0.299 + g*0.587 + b*0.114

# Seasoning the image =============================================

seasoned = np.copy(grayscale)
y,x = seasoned.shape
for yy in range(y):
  for xx in range(x):
    toSeasonOrNotToSeason = randint(0,255)
    if(toSeasonOrNotToSeason == 0 or toSeasonOrNotToSeason == 255):
      seasoned[yy][xx] = toSeasonOrNotToSeason

cv2.imshow("Original Grayscale", grayscale/255)
cv2.imshow("Seasoned Image", seasoned/255)
cv2.waitKey(0)
cv2.destroyAllWindows()

# preparing functions ====================================================

def mirrorPadding(size, array):
  new = np.copy(array)
  new = np.pad(new,((size,size),(size,size)),'reflect')
  return new

def meanFilter(size, array):
  y,x = array.shape
  mirrored = mirrorPadding(size,array)
  filtered = np.copy(array)
  for yy in range(size,size+y):
    for xx in range(size,size+x):
      mask = mirrored[yy-int(size/2):yy+int(size/2)+1,
                      xx-int(size/2):xx+int(size/2)+1]
      sum = 0
      for i in mask:
        for j in i:
          sum+=j
      filtered[yy-size][xx-size] = sum / (size*size)
  cv2.imshow(f"before Mean {size}*{size}", array/255)
  cv2.imshow(f"after Mean {size}*{size}", filtered/255)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  return filtered

def medianFilter(size, array):
  y,x = array.shape
  mirrored = mirrorPadding(size,array)
  filtered = np.copy(array)
  for yy in range(size,size+y):
    for xx in range(size,size+x):
      mask = mirrored[yy-int(size/2):yy+int(size/2)+1,
                      xx-int(size/2):xx+int(size/2)+1]
      maskarr = []
      for i in mask:
        for j in i:
          maskarr.append(j)
      maskarr.sort()
      filtered[yy-size][xx-size] = maskarr[int((size*size)/2)]
  cv2.imshow(f"before Median {size}*{size}", array/255)
  cv2.imshow(f"after Median {size}*{size}", filtered/255)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  return filtered

# executing the code =====================================================
meanFilter(3,seasoned)
meanFilter(5,seasoned)
medianFilter(3,seasoned)
medianFilter(5,seasoned)