import cv2

PATH = r"E:\PIC\201806.jpg"

img = cv2.imread(PATH)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow(imgpath, int(width*(height-80)/ pheight),height-80);
cv2.imshow("Image", img)
cv2.resizeWindow("Image", 640, 480)
cv2.waitKey(0)
cv2.destroyAllWindows()


