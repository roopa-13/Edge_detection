import cv2

img = cv2.imread("task1.png", cv2.IMREAD_GRAYSCALE)
img = img.astype(float)/255
imgx_new = img.copy()
imgy_new = img.copy()

sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

width, height = img.shape[:2]


# Convolution of the image with the sobel-x matrix
def convolution_x():
    for x in range(1, width-1):
        for y in range(1, height - 1):
            pixel_x = (sobel_x[0][0] * img[x-1, y-1]) + (sobel_x[0][1] * img[x, y-1]) + \
                      (sobel_x[0][2] * img[x+1, y-1]) + (sobel_x[1][0] * img[x-1, y]) +\
                      (sobel_x[1][1] * img[x, y]) + (sobel_x[1][2] * img[x+1, y]) +\
                      (sobel_x[2][0] * img[x-1, y+1]) + (sobel_x[2][1] * img[x, y+1]) +\
                      (sobel_x[2][2] * img[x+1, y+1])
            imgx_new[x, y] = pixel_x
    return imgx_new


# Convolution of the image with the sobel-y matrix
def convolution_y():
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            pixel_y = (sobel_y[0][0] * img[x - 1, y - 1]) + (sobel_y[0][1] * img[x, y - 1]) + \
                        (sobel_y[0][2] * img[x + 1, y - 1]) + (sobel_y[1][0] * img[x - 1, y]) + \
                        (sobel_y[1][1] * img[x, y]) + (sobel_y[1][2] * img[x + 1, y]) + \
                        (sobel_y[2][0] * img[x - 1, y + 1]) + (sobel_y[2][1] * img[x, y + 1]) + \
                        (sobel_y[2][2] * img[x + 1, y + 1])
            imgy_new[x, y] = pixel_y
    return imgy_new


cv2.imshow('Original- Flight Image', img)
cv2.imshow('Edge along x- Flight Image', convolution_x())
cv2.imshow('Edge along y- Flight Image', convolution_y())

cv2.waitKey(0)
cv2.destroyAllWindows()
