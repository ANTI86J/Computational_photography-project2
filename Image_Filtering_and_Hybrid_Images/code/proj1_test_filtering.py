'''
This script is used for testing my_imfilter()
Before using filters to construct the mixed image in PROJ1, you should verify that you have a reasonable output
All outputs are saved
'''


from gauss2D import gauss2D
from my_imfilter import my_imfilter
from skimage import transform
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os


def normalize(img):
	''' normalization'''
	img_min = img.min()
	img_max = img.max()
	return (img - img_min) / (img_max - img_min)
	
	
''' set the image '''
main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_path = main_path + '/data/cat.bmp'
test_image = mpimg.imread(img_path)
test_image = transform.resize(test_image, (255, 255))
plt.figure('Image')
plt.imshow(test_image)


''' filter '''
# Should the filter do nothing no matter what filling method is used
identity_filter = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=np.single)
identity_image  = my_imfilter(test_image, identity_filter)
plt.figure('Identity')
plt.imshow(identity_image)


''' Small blur with a box filter '''
#  remove some of the high frequencies
blur_filter = np.array([[1,1,1], [1,1,1], [1,1,1]])
blur_filter = blur_filter.astype(np.float) / np.sum(blur_filter)
blur_image = my_imfilter(test_image, blur_filter)
plt.figure('Box filter')
plt.imshow(normalize(blur_image))
plt.imsave(main_path+'/results/blur_image.png', normalize(blur_image + 0.5))

''' Large blur '''
# Gaussian blur is separable and fuzzy order in each direction.
large_2d_blur_filter = gauss2D(shape=(25, 25), sigma=10)
large_blur_image = my_imfilter(test_image, large_2d_blur_filter)
plt.figure('Gauss filter')
plt.imshow(normalize(large_blur_image))
plt.imsave(main_path+'/results/large_blur_image.png', normalize(large_blur_image + 0.5));


''' Directed filter (Sobel operator)  '''
sobel_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_image = my_imfilter(test_image, sobel_filter)

# Add 0.5 here because the output image is centered around 0, otherwise it is mostly black
plt.figure('Sobel filter')
plt.imshow(normalize(sobel_image+0.5))
plt.imsave(main_path+'/results/sobel_image.png', normalize(sobel_image + 0.5))


'''High pass filter (Discrete Laplacian filter)'''
laplacian_filter = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
laplacian_image = my_imfilter(test_image, laplacian_filter)

# Add 0.5 here because the output image is centered around 0, otherwise it is mostly black
plt.figure('Laplacian filter')
plt.imshow(normalize(laplacian_image+0.5))
plt.imsave(main_path+'/results/laplacian_image.png', normalize(laplacian_image + 0.5))


'''High pass "filter" alternative to get low frequencies'''
high_pass_image = test_image - blur_image

plt.figure('High pass filter')
plt.imshow(normalize(high_pass_image+0.5))
plt.imsave(main_path+'/results/high_pass_image.png', normalize(high_pass_image + 0.5))
plt.show()
print('All Set')