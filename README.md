# Computational_photography-project2
The goal of this project is to try to make a hybrid image, and to be more, to make a morphing gif

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

