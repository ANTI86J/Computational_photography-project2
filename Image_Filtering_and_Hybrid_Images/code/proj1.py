'''
Hybrid Image
'''

from my_imfilter import my_imfilter
from gauss2D import gauss2D
import numpy as np
import cv2
import matplotlib.image as mpimg
from PIL import Image
import matplotlib.pyplot as plt
import os

img1_name='bicycle'
img2_name='motorcycle'

#img1_name='dog'
#img2_name='cat'

#img1_name='einstein'
#img2_name='marilyn'

#img1_name='bird'
#img2_name='plane'

#img1_name='submarine'
#img2_name='fish'


cutoff_frequency = 7
# Standard deviation of pixels in gaussian blur


def normalize(img):
	'''  
	normalization
	'''
	img_min = img.min()
	img_max = img.max()
	return (img - img_min) / (img_max - img_min)


def setup_image(img1_name,img2_name):
	'''
	read the image and change the format to float
	'''
	main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	image1 = mpimg.imread(main_path + '/data/'+img1_name+'.bmp')
	image2 = mpimg.imread(main_path + '/data/'+img2_name+'.bmp')
	image1 = image1.astype(np.single)/255 
	image2 = image2.astype(np.single)/255
	return image1, image2, main_path


def gen_hybrid_image(image1, image2, cutoff_frequency):
	''' 
	使用my_imfilter创建“低频率”和“高频率”。组合它们来创建“混合图”。
	输入:
	- image1 : 提供低频
	- image2 : 提供高频
	- cutoff_frequency ::高斯模糊像素的标准差
	'''
	cutoff_frequency
	gaussian_filter = gauss2D(shape=(cutoff_frequency*4+1, cutoff_frequency*4+1), sigma=cutoff_frequency)
	low_frequencies = my_imfilter(image1, gaussian_filter)  
	high_frequencies = image2 - my_imfilter(image2, gaussian_filter)  
	hybrid_image = low_frequencies+high_frequencies  
	return low_frequencies, high_frequencies, hybrid_image


def vis_hybrid_image(hybrid_image):
	'''
	Visualize the mixed image by progressively sampling the image downward and connecting all the images together.
	'''
	scales = 5  
	scale_factor = 0.5  
	padding = 5  
	original_height = hybrid_image.shape[0]
	num_colors = hybrid_image.shape[2]  
	output = hybrid_image[:]
	cur_image = hybrid_image[:]
	for i in range(1, scales):
		output = np.concatenate((output, np.ones((original_height, padding, num_colors))), axis=1)  
		cur_image = cv2.resize(cur_image, (scale_factor*cur_image.shape[0], scale_factor*cur_image.shape[1]), interpolation=cv2.INTER_NEAREST).astype(np.float)/255.0
		tmp = np.concatenate((np.ones((original_height-cur_image.shape[0], cur_image.shape[1], num_colors)), cur_image), axis=0)
		output = np.concatenate((output, tmp), axis=1)
	return output
	
	
def save_image(main_path, low_frequencies, high_frequencies, hybrid_image, img1_name, img2_name):
	''' 
	save the image
	'''
	vis = vis_hybrid_image(hybrid_image)
	plt.imsave(main_path+'/results/low_frequencies_'+img1_name+'.png', normalize(low_frequencies))
	plt.imsave(main_path+'/results/high_frequencies_'+img2_name+'.png', normalize(high_frequencies+0.5))
	plt.imsave(main_path+'/results/hybrid_image_'+img1_name+'_'+img2_name+'.png', normalize(hybrid_image))
	plt.imsave(main_path+'/results/hybrid_image_scales_'+img1_name+'_'+img2_name+'.png', normalize(vis))


if __name__ == "__main__":
	image1, image2, main_path = setup_image(img1_name, img2_name)
	low_frequencies, high_frequencies, hybrid_image = gen_hybrid_image(image1, image2, cutoff_frequency)
	save_image(main_path, low_frequencies, high_frequencies, hybrid_image, img1_name, img2_name)