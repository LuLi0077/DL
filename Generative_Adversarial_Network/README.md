# Generative Adversarial Networks (GAN)

## Introduction

Build a generative adversarial network (GAN) trained on the MNIST dataset. From this, we'll be able to generate new handwritten digits.

GANs were [first reported on](https://arxiv.org/abs/1406.2661) in 2014 from Ian Goodfellow and others in Yoshua Bengio's lab. Since then, GANs have exploded in popularity. Here are a few examples to check out:

* [Pix2Pix](https://affinelayer.com/pixsrv/) 
* [CycleGAN](https://github.com/junyanz/CycleGAN)
* [A whole list](https://github.com/wiseodd/generative-models)

The idea behind GANs is that you have two networks, a generator $G$ and a discriminator $D$, competing against each other. The generator makes fake data to pass to the discriminator. The discriminator also sees real data and predicts if the data it's received is real or fake. The generator is trained to fool the discriminator, it wants to output data that looks _as close as possible_ to real data. And the discriminator is trained to figure out which data is real and which is fake. What ends up happening is that the generator learns to make data that is indistiguishable from real data to the discriminator.

![GAN diagram](images/gan_diagram.png)

The general structure of a GAN is shown in the diagram above, using MNIST images as data. The latent sample is a random vector the generator uses to contruct its fake images. As the generator learns through training, it figures out how to map these random vectors to recognizable images that can fool the discriminator.

The output of the discriminator is a sigmoid function, where 0 indicates a fake image and 1 indicates an real image. 

* `Intro_to_GANs.ipynb`


## Autoencoders

Build a simple autoencoder to compress the MNIST dataset. With autoencoders, we pass input data through an encoder that makes a compressed representation of the input. Then, this representation is passed through a decoder to reconstruct the input data. Generally the encoder and decoder will be built with neural networks, then trained on example data.

* `Simple_Autoencoder.ipynb`
* `Convolutional_Autoencoder.ipynb`
* `demo_generate_images.ipynb`


## [how_to_generate_video](https://github.com/llSourcell/how_to_generate_video)

This is the code for "How to Generate Video - Intro to Deep Learning #15' by Siraj Raval on YouTube

* `logograms.ipynb`


## Generate Faces

Use a generative adversarial network (GAN) to generate novel faces.


## Resources

* [Generative Models](https://blog.openai.com/generative-models/)
* Neural Information Processing Systems Conference - NIPS 2016: [Generative Adversarial Networks](https://channel9.msdn.com/Events/Neural-Information-Processing-Systems-Conference/Neural-Information-Processing-Systems-Conference-NIPS-2016/Generative-Adversarial-Networks)
* [An introduction to Generative Adversarial Networks (with code in TensorFlow)](http://blog.aylien.com/introduction-generative-adversarial-networks-code-tensorflow/)
* [Generative Adversarial Nets in TensorFlow](http://wiseodd.github.io/techblog/2016/09/17/gan-tensorflow/)
* [Improved Techniques for Training GANs](https://arxiv.org/pdf/1606.03498.pdf)

