import numpy
import argparse
import cv2
import os


def cv2_imread(img_path):
    cv_img = cv2.imdecode(numpy.fromfile(img_path, dtype=numpy.uint8), -1)
    return cv_img

PATH = r"E:\PIC\201806_2.jpg"
# PATH = r"E:\公司项目\VW\数羊\内蒙测试数据\201806.jpg"
# PATH = r"E:\公司项目\VW\数羊\内蒙测试数据\201.jpg"
# PATH = r"C:\Users\WANT\Pictures\t.png"
# PATH = r"E:\公司项目\VW\APP采集统计定制\四川部署\四川部署数据\20180109演示\00测试点数据转投影\仁寿县\001_1.tif"
if os.path.exists(PATH):
    image = cv2_imread(PATH)
    # cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)

# if don't use a floating point data type when computing
# the gradient magnitude image, you will miss edges
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = numpy.uint8(numpy.absolute(lap))

# display two images in a figure
cv2.namedWindow("Edge detection by Laplacaian", cv2.WINDOW_NORMAL)
cv2.imshow("Edge detection by Laplacaian", numpy.hstack([lap, gray]))

cv2.imwrite("1_edge_by_laplacian.jpg", numpy.hstack([gray, lap]))

if (cv2.waitKey(0) == 27):
    cv2.destroyAllWindows()

