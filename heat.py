import cv2 as cv
import numpy as np

img = cv.imread("fire.png")

w,h=int(img.shape[1]*0.3),int(img.shape[0]*0.3)

img = cv.resize(img,(w,h),interpolation=cv.INTER_AREA)

heat_map = np.zeros((h, w,3), dtype='uint8')


r=120
#bgr


ch=input("1-red\n2-green\n3-blue\ncolor : ")


if ch=="red":
    for i in range(h):
        for j in range(w):
            x,y,z=img[i][j]

            if x>r and y>r and z >r:
                heat_map[i][j] = [255, 255, 255]
            else:
                heat_map[i][j] = [255 - x, 255 - y, z]

elif ch == "green":
    for i in range(h):
        for j in range(w):
            x, y, z = img[i][j]

            if x > r and y > r and z > r:
                heat_map[i][j] = [255, 255, 255]
            else:
                heat_map[i][j] = [255 - x, y, 255 - z]

elif ch == "blue":
    for i in range(h):
        for j in range(w):
            x, y, z = img[i][j]

            if x > r and y > r and z > r:
                heat_map[i][j] = [255, 255, 255]
            else:
                heat_map[i][j] = [x, 255 - y, 255 - z]


cv.imshow("image",img)
cv.imshow("HeatMap",heat_map)
cv.waitKey(0)