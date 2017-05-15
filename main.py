import cv2
import numpy
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread("E:\\DeXel\\Desktop\\DEFo5Hd.jpg", 0)
    # cv2.imshow("image", img)
    # cv2.waitKey(0)

    print(cv2.__version__)
    scalar = 4
    nums = [[numpy.random.normal() * scalar for i in range(len(img[0]))] for j in range(len(img))]
    n, bins = numpy.histogram(nums, numpy.linspace(-3, 3, 7))

    noise_image = numpy.array(nums)

    cv2.imshow("image", noise_image + img)
    cv2.waitKey(0)