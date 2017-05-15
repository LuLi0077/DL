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

Epoch 1/2 Discriminator Loss: 1.5104 Generator Loss: 0.6003 | Epoch 2/2 Discriminator Loss: 1.2627 Generator Loss: 0.6249    
:----------------------------------------------------------:|:----------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/mnist1.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/mnist2.png" width="425" height="300">

* CelebA

Discriminator Loss: 0.8117 Generator Loss: 1.5095 | Discriminator Loss: 1.2518 Generator Loss: 1.1940    
:------------------------------------------------:|:------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba1.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba2.png" width="425" height="300">

Discriminator Loss: 1.0874 Generator Loss: 0.8658 | Discriminator Loss: 1.2037 Generator Loss: 0.8593   
:------------------------------------------------:|:------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba3.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba4.png" width="425" height="300">

Discriminator Loss: 1.4271 Generator Loss: 0.5355 | Discriminator Loss: 1.0541 Generator Loss: 1.0684    
:------------------------------------------------:|:------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba5.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba6.png" width="425" height="300">

Discriminator Loss: 1.1710 Generator Loss: 0.8174 | Discriminator Loss: 1.3247 Generator Loss: 0.5988   
:------------------------------------------------:|:------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba7.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Generate_Faces/assets/celeba8.png" width="425" height="300">

