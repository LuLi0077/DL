# Deep Convolutional GANs

Implement the Deep Convolutional Generative Adversarial Network(DCGAN) model to generate full color images. The additional complexity of these images requires using convolutional layers in the generator and discriminator. Batch normalization is also needed to get the GAN to train appropriately.

GAN is trained on the [Street View House Numbers (SVHN)](http://ufldl.stanford.edu/housenumbers/) dataset, a small example is shown below. After training, the generator will be able to create images that are nearly identical to these images.

![sample image](assets/32x32eg.png)


### Batch Normalization

Batch normalization is a technique for improving the performance and stability of neural networks. The idea is to normalize the layer inputs such that they have a mean of zero and variance of one, much like how we standardize the inputs to networks. Batch normalization is necessary to make DCGANs work.

* `Batch_Normalization.ipynb`
* `Batch_Normalization_Exercises.ipynb`

Comparisons between identical networks, with and without batch normalization: 

two networks using a ReLU activation function, a learning rate of 0.01, and reasonable starting weights |  two networks with the same hyperparameters used in the previous example, but only trains for 2000 iterations  
:------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp1.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp2.png" width="425" height="300">  

two networks using a sigmoid activation function, a learning rate of 0.01, and reasonable starting weights |  two networks using a ReLU activation function, a learning rate of 1, and reasonable starting weights 
:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp3.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp4.png" width="425" height="300">  

two networks using a sigmoid activation function, a learning rate of 1, and reasonable starting weights |  a similar pair of networks trained for only 2000 iterations 
:------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp5.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp6.png" width="425" height="300"> 

two networks using a ReLU activation function, a learning rate of 2, and reasonable starting weights |  two networks using a sigmoid activation function, a learning rate of 2, and reasonable starting weights 
:---------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp7.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp8.png" width="425" height="300"> 

two networks using a ReLU activation function, a learning rate of 0.01, and bad starting weights |  two networks using a sigmoid activation function, a learning rate of 0.01, and bad starting weights 
:-----------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp9.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp10.png" width="425" height="300"> 

two networks using a ReLU activation function, a learning rate of 1, and bad starting weights |  two networks using a sigmoid activation function, a learning rate of 1, and bad starting weights 
:--------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp11.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp12.png" width="425" height="300"> 

two networks using a ReLU activation function, a learning rate of 2, and bad starting weights |  two networks using a sigmoid activation function, a learning rate of 2, and bad starting weights 
:--------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp13.png" width="425" height="300">  |  <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/comp14.png" width="425" height="300"> 


### DCGAN Implementation

`DCGAN.ipynb` - 
* Getting the data
* Network inputs
* Generator (below is the archicture used in the original DCGAN paper)

![DCGAN Generator](assets/dcgan.png)

* Discriminator
* Model loss 
* Optimizers 
* Building the model 
* Hyperparameters (below are the sample generated images during training)

Epoch 1/10 Discriminator Loss: 0.4504 Generator Loss: 1.5919 | Epoch 2/10 Discriminator Loss: 0.6140 Generator Loss: 1.2087    
:-----------------------------------------------------------:|:-----------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen1.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen2.png" width="425" height="300">  

Epoch 3/10 Discriminator Loss: 1.0327 Generator Loss: 1.0601 | Epoch 4/10 Discriminator Loss: 1.3329 Generator Loss: 0.8090     
:-----------------------------------------------------------:|:-----------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen3.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen4.png" width="425" height="300"> 

Epoch 5/10 Discriminator Loss: 1.5532 Generator Loss: 1.0704 | Epoch 6/10 Discriminator Loss: 1.0467 Generator Loss: 1.2126     
:-----------------------------------------------------------:|:-----------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen5.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen6.png" width="425" height="300">

Epoch 7/10 Discriminator Loss: 1.6845 Generator Loss: 0.3241 | Epoch 8/10 Discriminator Loss: 0.9642 Generator Loss: 1.0499     
:-----------------------------------------------------------:|:-----------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen7.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen8.png" width="425" height="300">

Epoch 9/10 Discriminator Loss: 1.3002 Generator Loss: 1.1911 | Epoch 10/10 Discriminator Loss: 1.0263 Generator Loss: 1.1946     
:-----------------------------------------------------------:|:-----------------------------------------------------------:
<img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen9.png" width="425" height="300"> | <img src="https://github.com/LuLi0077/DL/blob/master/Generative_Adversarial_Network/Deep_Convolutiona_GANs/assets/gen10.png" width="425" height="300">


## Resources

* [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167.pdf)
* [Chapter 8: Optimization for Training Deep Models](http://www.deeplearningbook.org/contents/optimization.html)
* [Implementing Batch Normalization in Tensorflow](https://r2rt.com/implementing-batch-normalization-in-tensorflow.html)
* [Recurrent Batch Normalization](https://arxiv.org/pdf/1603.09025.pdf): [GitHub Repo](https://gist.github.com/spitis/27ab7d2a30bbaf5ef431b4a02194ac60)
* [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](https://arxiv.org/pdf/1511.06434.pdf)

