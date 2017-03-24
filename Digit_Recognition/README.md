# Handwritten Number Recognition with TFLearn and MNIST

Building a neural network that recognizes handwritten numbers using the **MNIST** data set, which consists of images of handwritten numbers and their correct labels 0-9. We'll be using [TFLearn](http://tflearn.org/), a high-level library built on top of TensorFlow to build the neural network.

For humans its easy to see that these numbers are 5, 0, 4, 1, 9, and 2, but for computers it can be a challenging problem.
![SampleDigits](https://github.com/LuLi0077/DL/blob/master/Digit_Recognition/SampleDigits.png)

## About the data

Each image of a handwritten number is 28 pixels in height and width, for a total of 784 pixels (28x28 = 784). And each pixel in an image, has a value associated with it that indicates how dark it is. So, we can think of an image as an array of 784 different pixel values.

In the MNIST data, this 2D array is flattened, meaning that it is represented in one dimension rather than two, and each image becomes a one dimensional array of 784 pixel values.

## Main steps

`Handwritten_Digit_Recognition_with_TFLearn.ipynb`
* Retrieving training and test data
* Visualize the training data
* Building the network
* Training the network
* Testing