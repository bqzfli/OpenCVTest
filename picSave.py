import cv2

PATH = r"E:\PIC\201806.jpg"
PATH_1_JPG = r"E:\PIC\201806_1.jpg"

img = cv2.imread(PATH)
img_1 = img.copy()
cv2.imwrite(PATH_1_JPG, img_1, [int(cv2.IMWRITE_JPEG_QUALITY), 5])

img_1 = cv2.imread(PATH_1_JPG)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()


