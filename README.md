# Computational_photography-project2
The goal of this project is to try to make a hybrid image, and to be more, to make a morphing gif

1. Project details:
First I collect some typical pictures, just like those:

![bicycle](https://user-images.githubusercontent.com/34802668/153700512-53a1503c-9174-4162-8cb4-e06e17a05e44.png)

![marilyn](https://user-images.githubusercontent.com/34802668/153700527-b747e156-8b82-4356-b088-c0d9d4244c74.png)

Then, I need to write the filter,like the detail said, I tried to implement the Gaussian filter, and the equation would be:

<img width="344" alt="image" src="https://user-images.githubusercontent.com/34802668/153701491-06140d4b-653e-4f24-968c-5c58c6a6688c.png">

so, according to this equation, I used numpy package to implement my 2D Gaussian filter, and then convolute the whole image using the filter, but then I found that, using this filter to convolute would lose some information around the edge, just like that:

<img width="186" alt="image" src="https://user-images.githubusercontent.com/34802668/153700861-9036f93f-f84f-442a-89cb-33ec7a0d2e01.png">

you can see some of the ears and months of the dog get clipped, so I need to use some '0' to fill the edge so that the shape of the image could be divisible by the shape of the filter size, just like that:

![low_frequencies_dog](https://user-images.githubusercontent.com/34802668/153700922-30ec8038-378f-4a48-a884-d4e26201b212.png)

and that's how I get the low frequency images. Then I use the impulse filter minus the Gaussian filter (which can be computed by subtracting the Gaussian-filtered image from the original) as you said in the project detail.Just like that:

![high_frequencies_marilyn](https://user-images.githubusercontent.com/34802668/153700993-bb138551-0ac7-45d0-a896-6f89c4b5a174.png)

![high_frequencies_plane](https://user-images.githubusercontent.com/34802668/153700999-a0d2964c-b693-4b83-9e8a-976a07fe7255.png)

and then, just hybrid it!But the prior problem is how to match up the size between those images,I have tried to use the Google API to locate the object and resize those images according to the proportion of the bounding size and the image size, but it's not worth that without a large scale of data in it, and for this project, I used some methods of data augmentation to make a bigger scale of data.Then I thought, what about rescale all the data so that the object in the pictures is all in the middle.So, at the end,I got this hybrid images:

![hybrid_image_submarine_fish](https://user-images.githubusercontent.com/34802668/153701387-8718ed8f-4c4a-4f48-825b-ae16054004c9.png)

using these two images:

![fish](https://user-images.githubusercontent.com/34802668/153701409-90d3b8a1-65c8-4f79-8f93-767ad33860b7.png)

![submarine](https://user-images.githubusercontent.com/34802668/153701422-a648a5e9-c1be-41e6-94b8-a3e58a4de6fb.png)

another examples would be:

1) original images:

![cat](https://user-images.githubusercontent.com/34802668/153701535-6ecadd77-52fb-4fa7-af70-88b60836d6e6.png)

![dog](https://user-images.githubusercontent.com/34802668/153701538-40c67b41-ebd3-4791-9ca6-368696fa0a4a.png)

and the hybrid result would be:

![hybrid_image_dog_cat](https://user-images.githubusercontent.com/34802668/153701549-d2b6ddc0-ded1-4e1d-8490-7ef9b5b27621.png)

2) original images:

![marilyn](https://user-images.githubusercontent.com/34802668/153701626-6b82969c-dc7c-4979-a07e-535ed7cb312d.png)

![einstein](https://user-images.githubusercontent.com/34802668/153701641-a6fef186-170f-41e0-bfe8-8af33d79ce65.png)

and the hybrid result would be:

![hybrid_image_einstein_marilyn](https://user-images.githubusercontent.com/34802668/153701662-1f4e8a60-53cc-4ae4-ae1a-8d067ed0c5f8.png)

3) original images:

![bicycle](https://user-images.githubusercontent.com/34802668/153917495-39b676f5-fcd4-4fb7-8b0c-a3cb6d77b00b.png)

![motorcycle](https://user-images.githubusercontent.com/34802668/153917581-513fede3-0f2c-4718-a9b8-28285ed82fc8.png)


and the hybrid result would be:

![hybrid_image_bicycle_motorcycle](https://user-images.githubusercontent.com/34802668/153917456-502d3c14-940a-4541-a6c0-413a92f5e22d.png)



For those images, I used the function you gave to compute and display the 2D Fourier transform, and the result would be :

<img width="344" alt="image" src="https://user-images.githubusercontent.com/34802668/153701760-b223c783-7e47-4f04-ae54-6eb2d69ecce4.png">


<img width="344" alt="image" src="https://user-images.githubusercontent.com/34802668/153701737-fee3d791-dfe2-4ae4-8658-606360bdd2f8.png">

<img width="344" alt="image" src="https://user-images.githubusercontent.com/34802668/153701770-82a0ce27-b41f-45aa-a39b-361956ebc5a0.png">

<img width="344" alt="image" src="https://user-images.githubusercontent.com/34802668/153917766-8b03012a-4c49-4279-8cdd-e3a423b5a4fc.png">



2.Bells & Whistles:

1) Generate a morphing gif:

The reason I thought of the following method is that for face morphing, all we need to do is to select some specific points in the first image and then find the corresponding one in the second image.When we find those points pair, the next thing we do is to make routes from one to the other so that we can generate the gif, so the model I used in it couldn't be more appropriate!

Luckily I have done one before, here is some details:

Using dlib and opencv to detect the face. Advices on working with facial landmarks with dlib and opencv https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/

the dlib model we used to detect face landmarks is put in the model folder

The facial landmark detector will give us the estimated location of 68 (x, y) pair coordinates that represent salient regions of the face, including eye, eyebrows, nose, mouth, and jawline.

Using inverse warping to do the morphing.Using Delaunay triangulation to organize each pair of feature points to a triangle.

the dlib model we used to detect face landmarks is put in the extra_lab/model folder
and the model will automatically locate the points of each triangle corresponding.Then generate the gif!

In that way, I can see how the face morphing in a gif file!

the original two images are:

![kanna](https://user-images.githubusercontent.com/34802668/153701990-9547fbf2-44f1-4809-8cc6-9f864085e500.png)

![lmy7](https://user-images.githubusercontent.com/34802668/153701995-6524c273-0b95-4245-8861-4f7cbe2a394e.png)

and the output mp4 would be (here gives the link):
https://www.bilibili.com/video/BV1NU4y1M7n4/

The problem of this project is that the quality of the morphing is determined by the first image in the model, because it is the standard of the whole morphing procedure.

2) using color to enhance the effect

First I transformed the color space from RGB to HSV, but it doesn't work well

![hybrid_image_dog_cat1](https://user-images.githubusercontent.com/34802668/153782688-30840125-d32b-4a81-8d9a-00c188379494.png)

Then I transformed the color space from RGB to LUV, the result is kind of fairy:

![hybrid_image_dog_cat1](https://user-images.githubusercontent.com/34802668/153782730-78eaedbf-be4c-424e-844a-9c9f1c4faa6a.png)

Then I transformed the color space from RGB to BGR, it seems like we have better color:

![hybrid_image_dog_cat1](https://user-images.githubusercontent.com/34802668/153782874-d9d3681d-02c1-4add-bdba-c5f7fcc9aa27.png)


Group Member:Jingzhou Shen
