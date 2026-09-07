import cv2
import numpy as np

def add_crosshairs_to_camera(img):
    h, w, _ = img.shape

    # left cross hair
    # img = cv2.circle(img, center = (w//4, h//2), radius=h//8, color=(0,0,255), thickness=3)

    # right cross hair
    img = cv2.circle(img, center = (w//4*3, h//2), radius=h//8, color=(0,0,255), thickness=3)


    return img



if __name__ == '__main__':
    cv2.imwrite('cross_hairs.png', add_crosshairs_to_camera(cv2.imread('test.png')))
