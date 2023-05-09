import cv2

image = cv2.imread("tshirt-img.png",cv2.IMREAD_UNCHANGED)

cv2.imshow("title",image)
cv2.waitKey()

Scale_percent = 50

width = int(image.shape[0]*Scale_percent/100)
Height = int(image.shape[1]*Scale_percent/100)

dsize = (width,Height)

out_put = cv2.resize(image,dsize)

cv2.imwrite('Tshirt_Image_50.png',out_put)
cv2.waitKey(0)