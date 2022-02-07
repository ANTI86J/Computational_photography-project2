'''
test function
'''
from gauss2D import gauss2D
from my_imfilter import my_imfilter
import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os

''' set the image '''
main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_path = main_path + '/data/cat.bmp'
test_image = mpimg.imread(img_path)
test_image = cv2.resize(test_image, (0.7 * test_image.shape[0], 0.7 * test_image.shape[1]), interpolation=cv2.INTER_LINEAR)
test_image = test_image.astype(np.single)/255
plt.figure('Image')
plt.imshow(test_image)
plt.show()