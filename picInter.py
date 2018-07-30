import cv2
import numpy

PATH = r"E:\PIC\201806.jpg"
PATH_2_JPG = r"E:\PIC\201806_2.jpg"

img = cv2.imread(PATH)
# CV_INTER_NN - 最近邻插值,
#
# CV_INTER_LINEAR - 双线性插值 (缺省使用)
#
# CV_INTER_AREA - 使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..
#
# CV_INTER_CUBIC - 立方插值.

img_2 = cv2.resize(img, (1024, 256), interpolation=cv2.INTER_CUBIC)
cv2.imwrite(PATH_2_JPG, img_2, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

img_2 = cv2.imread(PATH_2_JPG)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", numpy.hstack([img, img_2]))
cv2.waitKey(0)
cv2.destroyAllWindows()


