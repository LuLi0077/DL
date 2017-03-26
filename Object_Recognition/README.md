# Object Recognition

Build a neural network classify images from the [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html). The dataset consists of airplanes, dogs, cats, and other objects. The dataset will need to be preprocessed, then train a convolutional neural network on all the samples. 

`Object_Recognition.ipynb`:

1. Get the data

2. Explore the data

	The dataset is broken into batches to prevent the machine from running out of memory. The CIFAR-10 dataset consists of 5 batches, named `data_batch_1`, `data_batch_2`, etc.. Each batch contains the labels and images that are one of the following: airplane, automobile, bird, cat, deer, dog, frog, horse, ship or truck.

3. Implement preprocess functions
	- normalize: normalizes image data in the range of 0 to 1
	- one-hot encode: encodes labels to one-hot encodings
	- preprocess training, validation, and testing data

4. Build the network
	- input: the neural network needs to read the image data, one-hot encoded labels, and dropout keep probability
	- convolution and max pooling layer
	- flatten layer: change the dimension of input from a 4-D tensor to a 2-D tensor
	- fully-connected layer
	- output layer: apply a fully connected layer to `x_tensor` with the shape (*Batch Size*, *num_outputs*)
	- create convolutional model

5. Train the neural network
	- single optimization
	- print loss and validation accuracy
	- hyperparameters
	- train the model

6. Test model