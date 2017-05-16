# Generate Faces

Use a generative adversarial network (GAN) to generate novel faces

### `face_generation.ipynb` -

1. Get/explore/preprocess the data: [MNIST](http://yann.lecun.com/exdb/mnist/) and [CelebFaces Attributes (CelebA)](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) dataset (since the CelebA dataset is complex, we'll test the neural network on MNIST first. Running the GANs on MNIST will allow us to see how well the model trains sooner)

MNIST Sample Images | CelebA Sample Images   
:------------------:|:------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/mnist.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba.png" width="425" height="300">  

2. Build the Neural Network

* Input: implement the `model_inputs` function to create TF Placeholders for the Neural Network.
* Discriminator: implement `discriminator` to create a discriminator neural network that discriminates on `images`.
* Generator: implement `generator` to generate an image using `z`. 
* Loss: implement `model_loss` to build the GANs for training and calculate the loss.
* Optimization: implement `model_opt` to create the optimization operations for the GANs. 

3. Neural Network Training

* MNIST

Epoch 1/2 Discriminator Loss: 1.4041 Generator Loss: 0.6163 | Epoch 2/2 Discriminator Loss: 1.1726 Generator Loss: 0.9164    
:----------------------------------------------------------:|:----------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/mnist1.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/mnist2.png" width="425" height="300">

* CelebA

Discriminator Loss: 1.4917 Generator Loss: 0.6127 | Discriminator Loss: 1.3936 Generator Loss: 0.6625    
:------------------------------------------------:|:------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba1.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba2.png" width="425" height="300">


